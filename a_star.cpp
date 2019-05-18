#include <std.h>

/*
1.  Initialize the open list
2.  Initialize the closed list
    put the starting node on the open 
    list (you can leave its f at zero)

3.  while the open list is not empty
    a) find the node with the least f on 
       the open list, call it "q"

    b) pop q off the open list
  
    c) generate q's 8 successors and set their 
       parents to q
   
    d) for each successor
        i) if successor is the goal, stop search
          successor.g = q.g + distance between 
                              successor and q
          successor.h = distance from goal to 
          successor (This can be done using many 
          ways, we will discuss three heuristics- 
          Manhattan, Diagonal and Euclidean 
          Heuristics)
          
          successor.f = successor.g + successor.h

        ii) if a node with the same position as 
            successor is in the OPEN list which has a 
           lower f than successor, skip this successor

        iii) if a node with the same position as 
            successor  is in the CLOSED list which has
            a lower f than successor, skip this successor
            otherwise, add  the node to the open list
     end (for loop)
  
    e) push q on the closed list
    end (while loop) 
*/

#define ROW 10
#define COL 10

typedef pair<int, int> Pair;  // (row, col)
typedef Pair<double, Pair> pPair;  // (f, (row, col))

// Different from C where cell doesn't need struct declared every use
struct cell {
	int parent_i, parent_j;
	double f, g, h;
};

int is_valid_Pair(Pair point) {
	return ((0 <= point.first < ROW) &&
			(0 <= point.second < COL));
}

int is_unblocked(int grid[ROW][COL], Pair point) {
	return grid[point.first][point.second];
}

int reached_dest(Pair point, Pair dest) {
	return (point.first == dest.first && point.second == dest.second);
}

float calc_dist(Pair p1, Pair p2) {
	return 
}

Pair make_pair(row, col) {
	return pair<row, col>;
}


int run_astar(int grid[ROW][COL], Pair src, Pair dest) {
	// Check if src and dest are valid points in grid
	if (!is_valid_Pair(src)) {
		printf("Source not within grid bounds\n");
		return 0;
	}

	if (!is_valid_Pair(dest)) {
		printf("Destination not within grid bounds\n");
		return 0;
	}

	if (!is_unblocked(src) || !is_unblocked(dest)) {
		printf("Destination or source blocked, impossible to reach either\n");
		return 0;
	}

	if (reached_dest(src, dest)) {
		printf ("Already at destination\n"); 
		return 1;
	}

	// Represent 
	int closed_list[ROW][COL];
	memset(closed_list, 0, ROW * COL * sizeof(int));

	cell cell_details[ROW][COL];

	int i, j;
	for (i = 0; i < ROW; i++) {
		for (j = 0; j < COL; j++) {
			// set parents to dummy values
			cell_details[i][j].parent_i = -1;
			cell_details[i][j].parent_j = -1;

			// Set to max value so any real option will be more optimal
			cell_details[i][j].f = FLT_MAX;
			cell_details[i][j].g = FLT_MAX;
			cell_details[i][j].h = FLT_MAX;
		}
	}

	i = src.first;
	j = src.second;
	// parent of src is itself
	cell_details[i][j].parent_i = i;
	cell_details[i][j].parent_j = j;

	// Distance from src to itself is 0
	cell_details[i][j].f = 0;
	cell_details[i][j].g = 0;
	cell_details[i][j].h = 0;

	set<pPair> openList;
	openList.insert(make_pair(0.0, make_pair(i, j)));

	// While there are still nodes to be checked and solution hasn't been found
	while (!openList.empty()) {
		// Get next node and remove from the list
		pPair p = *openList.begin();
		openList.erase(openList.begin());

		for (i = p.first-1; i <= p.first+1; i++) {
			for (j = p.second-1; j <= p.second+1; j++) {
				pair<i, j> branch;
				if (is_valid_Pair(branch) && is_unblocked(branch)) {
					if (reached_dest(branch, dest)) {
						printf("Found Destination\n");
						cell_details[i][j].parent_i = src.first;
						cell_details[i][j].parent_j = src.second;

						cell_details[i][j].h = calc_dist(branch, dest);
						// Will be distance 1 from its parent, which has
						// some distance from source
						cell_details[i][j].g = branch.g + 1.0;
					}
				}
		}
	}
}

void 



