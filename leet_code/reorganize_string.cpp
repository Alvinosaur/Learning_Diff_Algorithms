#include <queue>
#include <utility>
#include <unordered_map>
#include <string>
#include <iostream>

using namespace std;

class Solution {
    struct CompareVal {
        bool operator()(pair<char, int> p1, pair<char, int>p2) {
            return p1.second < p2.second;
        }
    };

public:
    string reorganizeString(const string & S) {
        priority_queue<pair<char,int>, vector<pair<char,int>>, CompareVal> pq;
        // since we are guaranteed S will have lowercase letters, we could 
        // optimize memory usage by creating static array of 24 spaces for the 
        // 24 letters
        unordered_map<char, int> char_count;
        string res;
        res.reserve(S.size());
        // O(N) track number of times each char is in string
        for (char c : S) {
            if (char_count.find(c) != char_count.end()) ++char_count[c];
            else char_count[c] = 1;
        }

        // store in priority queue
        for (auto it = char_count.begin(); it != char_count.end(); ++it) {
            pq.push(*it);
        }
        
        char prev = -1;
        while (!pq.empty()) {
            // Get highest priority elem, pop from pq
            pair<char, int> top = pq.top();
            pq.pop();

            // if previous char added is same as cur, get next one
            if (top.first == prev) {
                // if no next char, impossible and give up
                if (pq.empty()) return "";
                pair<char, int> next = pq.top();
                pq.pop();

                // add next char before highest priority
                res += next.first;
                if (--next.second > 0) pq.push(next);
            }

            res += top.first;
            prev = top.first;
            if (--top.second > 0) pq.push(top);
        }
        return res;
    }
};

int main() {
    Solution A;
    string res = A.reorganizeString("aaabc");
    cout << res << endl;
    return 0;
    
}