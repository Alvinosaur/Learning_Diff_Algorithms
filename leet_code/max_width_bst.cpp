#include <cmath>
#include <vector>
#include <iostream>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
    vector<vector<int>> min_max;
    int max_dist = 0;
public:
    int widthOfBinaryTree(TreeNode* root) {
        if (root == NULL) return 0;
        vector<int> new_vec;
        this->min_max.push_back(new_vec);
        this->DFS(root->right, 1, 1);
        this->DFS(root->left, 1, -1);
        return this->max_dist;
    }
    
    void DFS(TreeNode* root, int level, int dist) {
        if (root == NULL) return;
        if (this->min_max.size() == level) {
            vector<int> new_vec{dist, dist};
            this->min_max.push_back(new_vec);
        }
        else {
            this->min_max[level][0] = min(
                this->min_max[level][0],
                dist);
            this->min_max[level][1] = max(
                this->min_max[level][1],
                dist);
            int min_val = this->min_max[level][0];
            int max_val = this->min_max[level][1];
            int in_btwn_min = pow(2, level) - pow(2, level-abs(min_val)) - 1;
            int in_btwn_max = pow(2, level) - pow(2, level-abs(max_val)) - 1;
            if (in_btwn_min + in_btwn_max > this->max_dist) {
                this->max_dist = in_btwn_min + in_btwn_max;
            }
        }
        this->DFS(root->right, level+1, dist+1);
        this->DFS(root->left, level+1, dist-1);
    }
};

int main() {
    Solution A;
    TreeNode* root = new TreeNode(0);
    TreeNode* right = new TreeNode(2);
    TreeNode* left = new TreeNode(1);
    root->right = right;
    root->left = left;
    cout << A.widthOfBinaryTree(root) << endl;
}