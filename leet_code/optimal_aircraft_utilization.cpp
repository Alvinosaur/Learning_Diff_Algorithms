#include <utility>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<pair<int, int>> find_optimal_routes(
            vector<pair<int, int>> & forward_routes,
            vector<pair<int, int>> return_routes,
            int max_travel_dist) {
        // O(MlogM)
        sort(return_routes.begin(), return_routes.end(), 
            [](pair<int, int> val1, pair<int, int> val2) {
                return val1.second < val2.second;}
        );
        // O(NlogM)
        int min_dist = INT_MAX;
        vector<pair<int, int>> best_forward_returns;
        for (pair<int, int> forward : forward_routes) {
            int best_return_indx = find_smaller_or_equal(return_routes, 
                max_travel_dist - forward.second);
            int dist = max_travel_dist - (
                forward.second + return_routes[best_return_indx].second);
            if (dist < 0) continue;
            int f_id = forward.first;
            int r_id = return_routes[best_return_indx].first;
            if (dist < min_dist) {
                best_forward_returns.clear();
                best_forward_returns.push_back(make_pair(f_id, r_id));
                min_dist = dist;
            }
            else if (dist == min_dist) {
                best_forward_returns.push_back(make_pair(f_id, r_id));
            }
        }
        return best_forward_returns;
    }

    int find_smaller_or_equal(vector<pair<int, int>> & routes, int target) {
        int l = 0, r = routes.size();
        while (l <  r) {
            int m = (l + r) / 2;
            if (routes[m].second < target) l = m+1;
            else if (routes[m].second > target) r = m;
            else return m;
        }
        return l;
    }
};


int main() {
    Solution A;
    // Test1
    vector<pair<int, int>> forward1({
        make_pair(1, 3000), make_pair(2, 5000), make_pair(3, 7000), 
        make_pair(4, 10000)
    });
    vector<pair<int, int>> return1({
        make_pair(1, 2000), make_pair(2, 3000), make_pair(3, 4000), 
        make_pair(4, 5000)
    });
    int max_dist1 = 10000;
    vector<pair<int, int>> res = (
        A.find_optimal_routes(forward1, return1, max_dist1));
    for (auto v : res) cout << v.first << ", " << v.second << endl;

}