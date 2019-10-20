def connect_color(grid):
    # set of all possible gridpoints on grid
    grid_set = set([(i, j) for i in range(len(grid)) 
                    for j in range(len(grid[i]))])
    max_count = 0
    max_color = ""
    
    # while some nodes unseen, continue searching
    while(len(grid_set) > 0): 
        # get new random node
        (i, j) = grid_set.pop()
        color = grid[i][j]
        count = dfs(grid, (i, j), grid_set)

        if count > max_count:
            max_color = color
            max_count = count

    return max_color, max_count
    

def dfs(grid, node, nodes_left):
    # bug with using this directions strategy: diagonal moves are possible
    # directions = [-1, 0, 1]
    # up, left, right, down
    moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    (i, j) = node
    color = grid[i][j]
    count = 1
    for (drow, dcol) in moves:
        # if already visited, skip
        if (i+drow, j+dcol) not in nodes_left: continue

        if grid[i+drow][j+dcol] == color:
            # visit this node
            nodes_left.remove((i+drow, j+dcol))

            # recursively search starting from that node
            count += dfs(grid, (i+drow, j+dcol), nodes_left)

    return count

grid = [
    ['red', 'green', 'green', 'yellow'],
    ['red', 'red', 'green', 'yellow'],
    ['blue', 'blue', 'green', 'yellow']
]
max_color, max_count = connect_color(grid)
print(max_color, max_count)
                



