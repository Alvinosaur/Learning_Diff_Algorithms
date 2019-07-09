#include <vector> 
#include <iostream>

using vec_it = std::vector<int>::iterator;

 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

class Solution {
public:
    TreeNode* constructMaximumBinaryTree(std::vector<int>& nums) {
        // Base case
        if (nums.size() == 0) return NULL;
        else if (nums.size() == 1) return new TreeNode(nums[0]);
        else {
            int max_ind = get_max(nums);
            TreeNode* new_node = new TreeNode(nums[max_ind]);
            std::vector<int> left(nums.begin(), nums.begin() + max_ind);
            std::vector<int> right(nums.begin() + max_ind + 1, nums.end());
            new_node->left = constructMaximumBinaryTree(left);
            new_node->right = constructMaximumBinaryTree(right);
            return new_node;
        }
    }
private:
    int get_max(std::vector<int>& nums) {
        int max_ind = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[max_ind]) max_ind = i;
        }
        return max_ind;
    }
};

int main() {
    std::vector<int> v({1, 2, 3});
    std::vector<int> v1(v.begin(), v.begin()+1);
    std::vector<int> v2(v.begin()+1, v.end());
    for (auto it : v1) std::cout << it << std::endl;
    std::cout << "v2:"  << std::endl;
    for (auto it : v2) std::cout << it << std::endl;
    auto it = v.begin();
    auto it2 = v.end() - 1;
    std::cout << (it2 - it) << std::endl;

    // Solution a = Solution();
    // a.constructMaximumBinaryTree(v);
    return 0;
}