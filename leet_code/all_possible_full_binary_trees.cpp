/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    unordered_map<int, vector<TreeNode*>> memo {
        {1, {new TreeNode(0)}}, {0, {}}
    };
public:
    vector<TreeNode*> allPossibleFBT(int N) {
        if (memo.find(N) == memo.end()) {
            vector<TreeNode*> sols;
            for (int i = 1; i < N; i++) {
                vector<TreeNode*> sub_sols1 = allPossibleFBT(i);
                vector<TreeNode*> sub_sols2 = allPossibleFBT(N-1-i);
                for (TreeNode* s1 : sub_sols1) {
                    for (TreeNode* s2 : sub_sols2) {
                        TreeNode* n1 = new TreeNode(0);
                        n1->left = s1;
                        n1->right = s2;
                        sols.push_back(n1);
                    }
                }
            }
            memo[N] = sols;
        }
        return memo[N];
    }
};

int main() {
  Solution A;
  vector<TreeNode*> sols = A.allPossibleFBT(5);
  return 0;
}