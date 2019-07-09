// runtime: 55.83%, mem: 9.37%
class Solution1 {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // O(N) store every first digit and its index
        vector<int> result;
        map<int, int> digits1;
        for (int i = 0; i < nums.size(); i++) {
            pair<int, int> digit_pair(nums[i], i);
            digits1.insert(digit_pair);
        }
        // O(N)
        for (int i = 0; i < nums.size(); i++) {
            int second_digit = target - nums[i];
            // O(logN)
            auto it = digits1.find(second_digit);
            if (it != digits1.end()) {
                // not same element twice
                if (it->second != i) {
                    result.push_back(i);
                    result.push_back(it->second);
                    return result;
                }
            }
        }
        return result;
        
    }
};

// runtime: 99%, mem: 19%
class Solution2 {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // O(N) store every first digit and its index
        vector<int> result;
        std::unordered_map<int, int> digits1;
        digits1.reserve(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            pair<int, int> digit_pair(nums[i], i);
            digits1.insert(digit_pair);
        }
        // O(N)
        for (int i = 0; i < nums.size(); i++) {
            int second_digit = target - nums[i];
            // O(logN)
            auto it = digits1.find(second_digit);
            if (it != digits1.end()) {
                // not same element twice
                if (it->second != i) {
                    result.push_back(i);
                    result.push_back(it->second);
                    return result;
                }
            }
        }
        return result;
        
    }
};