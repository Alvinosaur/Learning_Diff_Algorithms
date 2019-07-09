#include <math.h>
#include <string>
#include <set>
#include <iostream>

using namespace std;

// O(N^2): Brute force with set
int lengthSubstring(string::iterator start, string::iterator end) {
    std::set<char> seen_char;
    for (auto it = start; it != end; it++) {
        if (seen_char.find(*it) != seen_char.end()) return seen_char.size();
        seen_char.insert(*it);
    }
    return seen_char.size();
}

class Solution1 {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0;
        for (auto it = s.begin(); it != s.end(); it++) {
            int length = lengthSubstring(it, s.end());
            if (length > ans) ans = length;
        }
        return ans;
    }
};

// O(2N) = O(N): Sliding Window
class Solution2 {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0, n = s.length(), i = 0, j = 0;
        set<char> seen_char;
        while (i < n && j < n) {
            if (seen_char.find(s[j]) == seen_char.end()) {
                seen_char.insert(s[j++]);
                ans = fmax(ans, j - i);
            }
            else seen_char.erase(s[i++]);
        }
        return ans;
    }
};

void printRange(string s, int i, int j) {
    cout << s.substr(i, j-i) << endl;
}

// Wrong b/c edge case "pwwkew"
class Solution3 {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0, n = s.length(), i = 0, j = 0;
        set<char> seen_char;
        while (i < n && j < n) {
            printRange(s, i, j);
            if (seen_char.find(s[j]) == seen_char.end()) {
                ans = fmax(ans, j - i + 1);
            }
            else {
                seen_char.erase(s[i++]);
            }
            
            j++;
        }
        return ans;
    }
};

int main() {
    Solution2 sol;
    cout << sol.lengthOfLongestSubstring("pwwkew") << endl;
    return 0;
}
