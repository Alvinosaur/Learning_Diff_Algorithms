import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import yaml

from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
import tf
tf_transform = tf.TransformerROS()

import parse_rosbag


YAML_FILENAME = 'calibrated_transforms.yaml'
ARM_ID = 4
LIDAR_1_ID = 5
LIDAR_2_ID = 6
generic_rigid_name = "/phasespace_pose_"
default_velodyne_trans = np.array([
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0378],
    [0.0, 0.0, 0.0, 1.0]
])
yaml_transforms = {
    'arm_base_to_velodyne_left_model' : None,
    'arm_base_to_velodyne_right_model' : None,
    'velodyne_left_model_to_velodyne_left' : default_velodyne_trans,
    'velodyne_right_model_to_velodyne_right' : default_velodyne_trans
}


class YamlTransformWriter():
    """Class that assists with gathering average transform and writes to a yaml 
    file.
    """
    def __init__(self, trans_data):
        """Parses 4 x 4 transform into rotation and translation, stores these
        separately for the given transform name.
        
        Arguments:
            trans_data {dict of str : np.array((4, 4))} -- maps transform names to their full transformation matrix
        """
        self._data = dict()
        for name, trans in trans_data.items():
            self._data[name] = dict()
            self._store_trans(trans[:3, 3], name)
            self._store_rot(trans[:3, :3], name)
        
    def _store_rot(self, rot_mat, trans_name):
        """Stores roll, pitch, and yaw of rotation given the translation name 
        as a string to be stored in yaml file.
        
        Arguments:
            rot_mat {np.array((3, 3))} -- rotation matrix
            trans_name {str} -- name of transformation, should have been stored 
            in initialization.
        """
        r, p, y = YamlTransformWriter.rpy_from_mat(rot_mat)
        self._data[trans_name]['rpy'] = '%f %f %f' % (r, p, y)

    def _store_trans(self, trans_mat, trans_name):
        """Stores translation x, y, z as string to be stored in yaml flie.
        
        Arguments:
            trans_mat {List} -- [x, y, z]
            trans_name {str} -- translation corresponding to that transform
        """
        x, y, z = trans_mat
        self._data[trans_name]['xyz'] = '%f %f %f' % (x, y, z)
        
    def write_to_file(self, filename):
        """Stores all transforms in yaml file of given name.
        
        Arguments:
            filename {str} -- name of yaml filename.
        """
        with open(filename, 'w+') as yaml_file:
            yaml.dump(self._data, yaml_file, default_flow_style=False)

    @staticmethod
    def rpy_from_mat(rot_mat):
        """Calculates roll, pitch, and yaw from a 3 x 3 rotation matrix.
        
        Arguments:
            rot_mat {np.array((3, 3))} -- rotation matrix
        
        Returns:
            float, float, float -- roll, pitch, yaw (or 0, 0, 0 and prints out 
            of error)
        """
        try:
            r = math.atan2(rot_mat[2][1], rot_mat[2][2])
            p = math.atan2(-rot_mat[2][0], 
                        (rot_mat[2][2]**2 + rot_mat[2][1]**2)**0.5)
            y = math.atan2(rot_mat[1][0], rot_mat[0][0])
            return r, p, y
        except Exception as e:
            print("Couldn't find rpy because %s. Assuming no rotation." % e)
            return 0, 0, 0
    

def viz_transforms(transforms):
    """Visualizes transforms with matplotlib, showing 3D points, vectors, and 
    names.
    
    Arguments:
        transforms {dict str : np.array((4, 4))} -- dict that maps transforms by name to 4 x 4 transformation matrices.
    """
    plt3d = plt.figure().gca(projection='3d')

    # Ensure that the next plot doesn't overwrite the first plot
    ax = plt.gca()
    ax.hold(True)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    origin = np.array([[1], [1], [1], [1]])  # [1, 1, 1]
    ax.scatter(origin[0][0], origin[1][0], origin[2][0], color='red')
    for name, trans in transforms.items():
        p = trans.dot(origin)
        ax.text(p[0][0], p[1][0], p[2][0], name, color='black')
        ax.scatter(p[0][0], p[1][0], p[2][0], color='green')
        ax.plot([origin[0][0], p[0][0]], [origin[1][0], p[1][0]], 
                zs=[origin[2][0], p[2][0]])

    plt.show()


def get_avg_pose(bag_data, topic_name):
    """Finds average translation and rotation of specific pose
    in a rosbag. 

    Translation found by simply averaging the x, y, z translations.


    
    Arguments:
        bag_data {dict(str: List[PoseStamped])} -- map topic name to list 
            of poses
        topic_name {str} -- name of topic from which to get pose
    
    Returns:
        List, List -- trans: [x, y, z], rot(quaternion): [x, y, z, w]
    """
    avg_trans = [0.0, 0.0, 0.0]
    avg_r, avg_p, avg_y = 0, 0, 0  # roll, pitch, yaw
    N = len(bag_data[topic_name])
    if N < 1: print('No data found!')
    for g_msg in bag_data[topic_name]:
        # translation
        x = g_msg.pose.position.x
        y = g_msg.pose.position.y
        z = g_msg.pose.position.z
        avg_trans[0] += float(x) / N
        avg_trans[1] += float(y) / N
        avg_trans[2] += float(z) / N

        # accumulate rotation
        Q = (g_msg.pose.orientation.x, g_msg.pose.orientation.y,
             g_msg.pose.orientation.z, g_msg.pose.orientation.w)
        r, p, y = tf.transformations.euler_from_quaternion(Q)
        avg_r += float(r) / N
        avg_p += float(p) / N
        avg_y += float(y) / N

    avg_quaternion = (tf.transformations.quaternion_from_euler(
        avg_r, avg_p, avg_y))

    return avg_trans, avg_quaternion


def main(viz=False):
    """Runs the script that parses a bag file to calculate
    static transform between the robot's two lidars and the arm position.

    Stores resulting transformations in a yaml file called 
    'calibrated_transforms.yaml' in current directory. 
    
    Keyword Arguments:
        viz {bool} -- whether to visualize average transformation with matplotlib (default: {False})
    """
    bagfile = parse_rosbag.get_bagfile()
    if bagfile is None: return
    pose_data = parse_rosbag.parse_bag(bagfile)

    # lidar-world
    lidar1_trans, lidar1_rot = get_avg_pose(pose_data, 
        generic_rigid_name + str(LIDAR_1_ID))
    lidar1_mat = tf_transform.fromTranslationRotation(
        lidar1_trans, lidar1_rot)

    lidar2_trans, lidar2_rot = get_avg_pose(pose_data, 
        generic_rigid_name + str(LIDAR_2_ID))
    lidar2_mat = tf_transform.fromTranslationRotation(
        lidar2_trans, lidar2_rot)

    # arm-world
    arm_trans, arm_rot = get_avg_pose(pose_data, 
        generic_rigid_name + str(ARM_ID))
    arm_mat = tf_transform.fromTranslationRotation(arm_trans, arm_rot)

    # lidar-arm = lidar-world * arm-world
    yaml_transforms['arm_base_to_velodyne_left_model'] = (
        lidar1_mat.dot(np.linalg.inv(arm_mat)))
    yaml_transforms['arm_base_to_velodyne_right_model'] = (
        lidar2_mat.dot(np.linalg.inv(arm_mat)))

    yaml_data = YamlTransformWriter(yaml_transforms)
    yaml_data.write_to_file(YAML_FILENAME)
    print('Wrote transforms to file: %s' % YAML_FILENAME)

    if viz:
        viz_transforms(yaml_transforms)
    

def test():
    """Basic test of usage with two transformations. 'fake' transformations
    all involve translation of 1, 1, 1 and rotation about z-axis by +90deg. The
    average should thus be the same. Verification can be done with the plot or by looking at the written file, 'fake.yaml'. 

    The second transformation expects average translation of 0, 0, 0 and 
    rotation of +90 about x and +45 about y.
    """
    fake_data = {'fake': [], 'fake2': []}
    for i in range(4):
        # trans 1, 1, 1, rot aobut z-axis by +90 deg
        t = Point(x=1, y=1, z=1)
        q = Quaternion(x=0, y=0, z=0.7071068, w=0.7071068)
        p = Pose(t, q)
        A = PoseStamped(pose=p)
        fake_data['fake'].append(A)

        # avg: trans 0, 0, 0, rot about x-axis +135, y-axis by -45
        if i % 2 == 0:
            # trans 2, 0, 1, rot aobut x-axis by +180 deg, y-axis by +90
            t = Point(x=2, y=0, z=1)
            q = Quaternion(x=0.7071068, y=0, z=-0.7071068, w=0)
            p = Pose(t, q)
            A = PoseStamped(pose=p)
            fake_data['fake2'].append(A)
        else:
            # trans -2, 0, -1, rot aobut x-axis by +90 deg
            t = Point(x=-2, y=0, z=-1)
            q = Quaternion(x=0.7071068, y=0, z=0, w=0.7071068)
            p = Pose(t, q)
            A = PoseStamped(pose=p)
            fake_data['fake2'].append(A)

    
    # Test Averaging of Translation and Rotation
    trans, rot = get_avg_pose(fake_data, 'fake')
    trans2, rot2 = get_avg_pose(fake_data, 'fake2')
    mat = tf_transform.fromTranslationRotation(trans, rot)
    mat2 = tf_transform.fromTranslationRotation(trans2, rot2)
    trans_map = {'fake': mat, 'fake2': mat2}
    yaml_data = YamlTransformWriter(trans_map)
    yaml_data.write_to_file('fake.yaml')
    viz_transforms(trans_map)


main(True)
# test()
    