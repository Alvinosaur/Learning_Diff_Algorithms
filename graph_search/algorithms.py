import collections
import heapq

import visualizer as viz

class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        if id in self.edges: return self.edges[id] 
        else: return None


class Queue:
    def __init__(self):
        self.items = collections.deque()

    def empty(self):
        return len(self.items) == 0

    def add(self, item):
        self.items.append(item)

    def get(self):
        if self.empty(): 
            print('Queue empty')
            return None
        else: return self.items.popleft()


class PriorityQueue:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def add(self, item, priority):
        heapq.heappush(self.items, (priority, item))

    def get(self):
        return heapq.heappop(self.items)[1]


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
    
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id):
        return id not in self.walls
    
    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results


class WeightedGrid(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)


def heuristic(a, b):
    (x1, y1), (x2, y2) = a, b
    return abs(x2 - x1) + abs(y2 - y1)


def BFS(graph, start, goal):
    """BFS: breadth_first_search
    
    Arguments:
        graph {SquareGrid} -- a graph of open spaces and obstacles
        start {Tuple(row, col)} -- starting location on graph
    """
    frontier = Queue()
    frontier.add(start)
    came_from = {}
    while not frontier.empty():
        current = frontier.get()
        if current == goal: break  # if reached goal, done
        for next in graph.neighbors(current):
            if next not in came_from:  # if never visited
                frontier.add(next)
                came_from[next] = current

    return came_from

def dijkstra_search(graph, start, goal):
    """Dijkstra's Search
    
    Arguments:
        graph {WeightedGrid} -- [description]
        start {[type]} -- [description]
        goal {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    frontier = PriorityQueue()
    frontier.add(start, 0)
    came_from = {}
    came_from[start] = None
    cost_so_far = {}
    cost_so_far[start] = 0
    path = {}
    i = 0
    while not frontier.empty():
        current = frontier.get()
        path[current] = i
        i += 1
        if current == goal: break
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + 1 # + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                came_from[next] = current
                # risk of duplicate after insertion, but dealt with by heapq
                frontier.add(next, new_cost)
    
    return came_from, cost_so_far, path


def greedy_depth_first(graph, start, goal):
    frontier = PriorityQueue()
    frontier.add(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0 # heuristic(start, goal)
    path = {}
    i = 0

    while not frontier.empty():
        current = frontier.get()
        path[current] = i
        i += 1
        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = heuristic(next, goal)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.add(next, priority)
                came_from[next] = current

    return came_from, cost_so_far, path


def a_star_search(graph, start, goal):
    """A* search
    
    Arguments:
        graph {WeightedGrid} -- [description]
        start {[type]} -- [description]
        goal {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    frontier = PriorityQueue()
    frontier.add(start, 0)
    came_from = {}
    came_from[start] = None
    cost_so_far = {}
    cost_so_far[start] = 0
    cost_with_priority = {}
    cost_with_priority[start] = 0 # heuristic(start, goal)
    path = {}
    i = 0
    while not frontier.empty():
        current = frontier.get()
        path[current] = i
        i += 1
        if current == goal: break
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + 1# + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                # including heuristic makes exploration towards goal a priority
                priority = new_cost + heuristic(next, goal)
                cost_with_priority[next] = priority
                frontier.add(next, priority)
                came_from[next] = current
                
    
    return came_from, cost_so_far, cost_with_priority, path


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse() #  reverse (goal -> start) to (start -> goal)
    return path


def test_BFS():
    print('BFS:')
    g = SquareGrid(30, 15)
    g.walls = viz.DIAGRAM1_WALLS
    start = (8, 7)
    goal = (17, 2)

    parents = BFS(g, start=start, goal=goal)
    viz.draw_grid(g, width=2, point_to=parents, start=start, goal=goal)

def test_weighted_search(graph_name):
    print(graph_name)
    start = (2, 6)
    goal = (7, 8)
    width = 3
    if graph_name == 'a_star': 
        came_from, cost_so_far, cost_with_priority, path = (
            a_star_search(viz.diagram4, start=start, goal=goal))
    elif graph_name == 'greedy':
        came_from, cost_so_far, path = (
            greedy_depth_first(viz.diagram4, start=start, goal=goal))
    else: 
        came_from, cost_so_far, path = (
            dijkstra_search(viz.diagram4, start=start, goal=goal))

    # viz.draw_grid(viz.diagram4, width, point_to=came_from, start=start, goal=goal)
    # print()
    viz.draw_grid(viz.diagram4, width, number=cost_so_far, start=start, goal=goal)
    # viz.draw_grid(viz.diagram4, width, number=cost_with_priority, start=start, goal=goal)
    print()
    viz.draw_grid(viz.diagram4, width, 
        path=reconstruct_path(came_from, start=start, goal=goal))


test_weighted_search('greedy')
test_weighted_search('dijkstra')
test_weighted_search('a_star')



