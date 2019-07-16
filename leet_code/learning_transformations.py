import numpy as np
import matplotlib.pyplot as plt
import math

RAD_TO_DEG = 180 / math.pi

"""
Turning point defined in B-frame back into A-frame
In B frame, point seems to be (x, y) = (1, 0)
but since B is +90deg rotated wrt A, imagine B is rotaed clockwise by +90
this means (1, 0) in normal A frame really is (0, -1)
"""
q_b = np.array([[1], [0]])
R_AB = np.array([[0, 1],
                [-1, 0]])
q_a = R_AB.dot(q_b)
print('q_a:')
print(q_a)
print('q_a back to B frame:')
print(np.linalg.inv(R_AB).dot(q_a))  # R_AB^-1 * q_a

"""
Shows composition of transformations.
"""
p_ab = np.array([[1], [1]])    # translation from a to b wrt a
R_AB = np.array([[0, 1],       # same rotation of +90deg
                [-1, 0]])
p_bc = np.array([[1], [-1]])   # translation from b to c wrt b
R_BC = np.array([[0, 1],       # same rotation of +90deg
                [-1, 0]])
R_AC = R_AB.dot(R_BC)          # B +90 wrt A, C +90 wrt B, so C +180 wrt A
print('R_AC, angle = %f' % (math.acos(R_AC[0][0]) * RAD_TO_DEG))
print(R_AC)

p_ac = p_ab + R_BC.dot(p_bc)   # Just draw it out, you'll see why this works
print('p_ac:')
print(p_ac)

"""
Shows the problem we faced with lidar to arm frame, where we were given both 
lidar and arm frame defined in global frame.
"""
p_ab = np.array([[1], [1]])
R_AB = np.array([[0, 1],       # same rotation of +90deg
                [-1, 0]])
p_ac = np.array([[2], [2]])    # (-1, 1) in B frame
R_AC = np.array([[0, 1],       # same rotation of +90deg
                [-1, 0]])
r_bc = p_ac - p_ab  # trans vector from b to c in A frame
p_bc = np.linalg.inv(R_AB).dot(r_bc)
print('p_bc:')
print(p_bc)

# should be 0 since both are rotated same wrt A
R_BC = np.linalg.inv(R_AB).dot(R_BC)  
print('R_BC, angle = %f' % (math.acos(R_BC[0][0]) * RAD_TO_DEG))
print(R_BC)
# fig = plt.figure()
# ax = fig.add_subplot(111)
# plt.scatter(p[0], p[1])
# plt.grid()
# plt.show()