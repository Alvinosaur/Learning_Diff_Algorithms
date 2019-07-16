#include <bits/stdc++.h> 
#include <algorithm>
typedef vector<vector<int>> vec_tuples;

// NOTE: doesn't compile, "double-free error"
class Solution {
    vec_tuples moves {
        {1, 0}, {0, -1}, {0, 1}, {0, 1}
    };
    vec_tuples grid;
    vec_tuples unseen;
    
    int in_bound(int row, int col) {
        return ((0 <= row && row < this->grid.size()) && 
                (0 <= col && col < this->grid[row].size()));
    }
    
    int paths_helper(int row, int col) {
        int total = 0;
        for (vector<int> move : moves) {
            int new_row = row + move[0];
            int new_col = col + move[1];
            if (!in_bound(new_row, new_col)) continue;
            vector<int> new_pos{new_row, new_col};
            
            // Case 1: visit unvisited node, make move recursive
            if (this->grid[new_row][new_col] == 0) {
                // make move
                this->grid[new_row][new_col] = 1;
                auto it = std::find(this->unseen.begin(), this->unseen.end(), 
                                    new_pos);
                std::swap(*it, this->unseen.back());
                this->unseen.pop_back();  // remove 
                
                total += this->paths_helper(new_row, new_col);
                
                // undo move
                this->grid[new_row][new_col] = 0;
                this->unseen.push_back(new_pos);
            }
            
            // Case 2: visit goal
            else if (this->grid[new_row][new_col] == 2) {
                // if seen all nodes, done, return 1
                if (this->unseen.size() == 1 && this->unseen[0] == new_pos) {
                    total++;
                }
            }
        }
        return total;
    }
public:
    int uniquePathsIII(vec_tuples& grid) {
        // generate unseen vector
        this->grid = grid;
        
        int start_r = 0, start_c = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.size(); j++) {
                if (grid[i][j] == 0 || grid[i][j] == 2) {
                    vector<int> pos{i, j};
                    this->unseen.push_back(pos);
                }
                else if (grid[i][j] == 1) {
                    start_r = i;
                    start_c = j;
                }
            }
        }
        return this->paths_helper(start_r, start_c);
    }
};
