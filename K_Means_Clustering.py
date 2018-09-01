import datetime
import logging
import json
import os
from random import randint
import matplotlib.pyplot as pp
import typing as t

logger = logging.Logger(__name__)

SEC_TO_HOUR = 1/(60 * 60)
START_HOUR = 4
START_MINUTE = 30


def get_existing_data(file_path: str) -> list:
    with open(file_path, 'r') as file:
        try:
            data = json.loads(file.read())
            return data['all_idle_timestamps']
        except (json.JSONDecodeError, KeyError):
            file_name = os.path.sep.split(file_path)[-1]
            logger.exception(f'Wrongly formatted file: {file_name}')


def normalize_data(timestamps_list: list) -> list:
    time_in_seconds = []
    for timestamp in timestamps_list:
        datetime_obj = datetime.datetime.fromtimestamp(timestamp)
        start_time = datetime_obj.replace(hour=START_HOUR, minute=START_MINUTE)
        difference = (datetime_obj - start_time).seconds
        time_in_seconds.append(difference)
    return time_in_seconds


def assign_clusters(data_points: t.List, clusters: t.List):
    """
    :param data_points: idle_data's all_idle_timestamps_key maps to a list
    of every timestamp in which the pnp machine and its computer was deemed
    idle (not including the required 10 minute threshold window of inactivity)

    :param clusters: list containing each cluster's value(timestamp)

    :return: list of tuples(assignment, cost), i:
        timestamp, i, is mapped to one cluster, k
        cost: this mapping's cost(distance from cluster to point)
    """
    cluster_groups = [[] for k in range(len(clusters))]
    assignment_with_costs = [(0, 0) for i in range(len(data_points))]
    for i in range(len(data_points)):
        timestamp = data_points[i]
        min_distance = clusters[0]  # temporarily assign to a value
        for k in range(len(clusters)):
            distance = abs(clusters[k] - timestamp)
            if distance < min_distance:
                min_distance = distance
                assignment_with_costs[i] = (k, min_distance)
        min_k = assignment_with_costs[i][0]  # cluster index with min distance
        # assign data point to the min_k cluster
        cluster_groups[min_k].append(data_points[i])
    return assignment_with_costs, cluster_groups


def initialize_clusters(data_points: t.List, K: int) -> list:
    """
    Given number of clusters, K, and the number of possible indexes, return a
    list of length K containing the randomly assigned indexes that map a
    cluster location to a value.

    :param data_points: list of all timestamps
    :type: list

    :param K: number of clusters
    :type: int

    :return: list of random indexes
    :type: list
    """
    init_cluster_points = []
    for k in range(K):
        random_index = randint(0, len(data_points) - 1)
        init_cluster_points.append(data_points[random_index])
    return init_cluster_points


def recalculate_cluster_values(groups: t.List) -> list:
    """

    :param groups: 2D list of length K clusters that contains all the data points
    assigned to each cluster

    :return: 1D list of K clusters where each value is the cluster's new
    value, defined as the mean of that cluster's assigned data points
    """
    ignored_clusters = []
    new_clusters = []
    for k in range(len(groups)):
        try:
            # calculate new cluster location based on mean of data points
            group_mean = sum(groups[k])/len(groups[k])
            new_clusters.append(group_mean)
        except ZeroDivisionError:
            continue
    return new_clusters


def run_k_means(data_values: t.List, clusters: t.List,
                num_iters=0, max_iters=10):
    """
    Runs for max_iters iterations to optimize costs of clusters
    :param data_values: list of all data values (ie: training examples)
    :param clusters: list of cluster values
    :param num_iters: track how many iterations have occurred
    :param max_iters: max number of iterations
    :returns:
        (assignment, cost) tuples for each i example
        list of optimized cluster values(a timestamp)
    """
    assignments_costs, cluster_groups = assign_clusters(data_values, clusters)
    new_clusters = recalculate_cluster_values(cluster_groups)
    if num_iters >= max_iters:
        # calculate the costs and groups of final cluster locations
        assignments_costs, cluster_groups = assign_clusters(data_values,
                                                            clusters)
        return assignments_costs, new_clusters
    return run_k_means(data_values, new_clusters, num_iters+1)


def calc_cluster_cost(assignment_cost_tuples, cluster_vals):
    """
    Calculates the total cost of each cluster, k
    :param assignment_cost_tuples: (assignment, cost) tuples of length, m
    examples

    :param cluster_vals: list of length K clusters where each value is
    cluster[k]'s value

    :return: total cost of all clusters
    """
    cluster_costs = 0
    for i in range(len(assignment_cost_tuples)):  # m examples
        k, cost = assignment_cost_tuples[i]
        cluster_costs += cost
    return cluster_costs


def plot_data(clusters, data_points):
    y_vals = [10]*len(data_points)
    cluster_y_vals = [10]*len(clusters)
    pp.plot(data_points, y_vals, 'r+', clusters, cluster_y_vals, 'bo')
    pp.show()


def main():
    idle_data = []
    all_folders = ['/home/alvin/Documents/pnp_logging/activity_data_machine_1/total_idle_time']
    for folder in all_folders:
        for file_name in os.listdir(folder):
            file_path = os.path.join(folder, file_name)
            data = get_existing_data(file_path)
            norm_data = normalize_data(data)
            idle_data.extend(norm_data)
    all_clusters, all_cluster_costs = [], []
    for k in range(1, 10):
        for num_trials in range(20):
            initial_clusters = initialize_clusters(idle_data, k)
            final_assignments_and_costs, final_clusters = (
                run_k_means(idle_data, initial_clusters))
            cost = calc_cluster_cost(final_assignments_and_costs,
                                     final_clusters)
            all_clusters.append(final_clusters)
            all_cluster_costs.append(cost)
            print('k: ', k, 'cost: ', cost)
    min_cost, min_cluster_index = all_cluster_costs[0], 0
    for index in range(1, len(all_clusters)):
        if all_cluster_costs[index] < min_cost:
            min_cost = all_cluster_costs[index]
            min_cluster_index = index
    print('Most Prominent Dead Zones: ', all_clusters[min_cluster_index])
    print('Error of these groupings in minutes', min_cost/60)
    plot_data(all_clusters[min_cluster_index], idle_data)

if __name__ == '__main__':
    main()
