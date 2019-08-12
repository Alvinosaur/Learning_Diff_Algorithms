#include <algorithm>
#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

class Solution {
    float euc_dist(int a, int b) {return pow(a*a + b*b, 0.5);}
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        sort(points.begin(), points.end(), [this](vector<int> a, vector<int> b){
            return euc_dist(a[0], a[1]) < euc_dist(b[0], b[1]);
        });
        auto first = points.begin();
        auto end = first + K;
        vector<vector<int>> result(first, end);
        return result;
    }
};


int main() {
    Solution A;
    vector<vector<int>> test({
        {3,3}, {5, -1}, {-2, 4}
    });
    vector<vector<int>> res = A.kClosest(test, 2);
    for (auto coord : res) cout << coord[0] << ", " << coord[1] << endl;
    return 0;
}