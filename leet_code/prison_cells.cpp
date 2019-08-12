#include <vector>
#include <map>
#include <utility>
#include <iostream>
#include <iterator>

using namespace std;

class Solution {
    map<vector<int>, int> iter_to_res;
public:
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        if (N == 0) return cells;
        pair<vector<int>, int> new_res = make_pair(cells, 0);
        iter_to_res.insert(new_res);
        for (int i = 1; i < N+1; i++) {
            udpate_cells(cells);
            if (i == 1) {
                cells[0] = 0;
                cells[cells.size()-1] = 0;
            }
            print_cells(cells);
            if (iter_to_res.find(cells) != iter_to_res.end()) {
                // Found a recurring pattern
                int res_index = N % iter_to_res.size();
                cout << "index: " << res_index << endl;
                auto it = iter_to_res.begin();
                advance(it, res_index);
                return it->first;
            }
            new_res = make_pair(cells, i);
            iter_to_res.insert(new_res);
        }
        return cells;
    }
    
    void print_cells(vector<int>& cells) {
        for (auto it : cells) cout << it << ", ";
        cout << endl;
    }
private:
    void udpate_cells(vector<int>& cells) {
        char prev_val = cells[0];  // implicitly cast btwn int and char 1, 0's
        char new_val = 0;
        for (int i = 1; i < cells.size()-1; i++) {
            new_val = !XOR(prev_val, cells[i+1]);
            prev_val = cells[i];
            cells[i] = new_val;
        }
    }
    
    int XOR(char val1, char val2) {
        return (val1 != val2);
    }
};

int main() {
    vector<int> cells = {1, 0, 1, 0};
    Solution A;
    A.print_cells(cells);
    A.prisonAfterNDays(cells, 4);
    cout << "result: " << endl;
    A.print_cells(cells);
    return 0;
}