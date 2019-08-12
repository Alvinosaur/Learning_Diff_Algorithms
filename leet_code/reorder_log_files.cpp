#include <algorithm>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

/*
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.
*/

struct comparator
{
    bool is_letter(const string &s, int & first_space) {
        int space_count = 0;
        int i = 0;
        for (i = 0; !space_count; ++i) {
            space_count = (s[i] == ' ');
        }
        first_space = i-1;
        return 'A' <= s[first_space+1] && s[first_space+1] <= 'z';
    }

    inline bool operator() (const string &log1, const string &log2) {
        int log1_first, log1_second, log2_first, log2_second;
        bool log1_letter = is_letter(log1, log1_first);
        bool log2_letter = is_letter(log2, log2_first);
        if (log1_letter == log2_letter) {
            if (log1_letter) {
                string log1_substr = log1.substr(log1_first+1, 
                        log1.size()-(log1_first+1));
                string log2_substr = log2.substr(log2_first+1, 
                        log2.size()-(log2_first+1));
                if (log1_substr == log2_substr) {
                    string log1_id = log1.substr(0, log1_first);
                    string log2_id = log2.substr(0, log1_first);
                    return log1_id < log2_id;
                }
                else return log1_substr < log2_substr;
            }
            else return false; // digit logs put in original order
        }
        else return log1_letter;
    }
};

class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        sort(logs.begin(), logs.end(), comparator());
        return logs;
    }
};


int main() {
    Solution A;
    vector<string> input({
        "l5sh 6 3869 08 1295", "16o 94884717383724 9", "43 490972281212 3 51", "9 ehyjki ngcoobi mi", "2epy 85881033085988", "7z fqkbxxqfks f y dg", "9h4p 5 791738 954209", "p i hz uubk id s m l", "wd lfqgmu pvklkdp u", "m4jl 225084707500464", "6np2 a"
    });
    vector<string> test({
        "a8 act zoo", "b 28 3", "a7 act zoo", "b 9 0", "c 8 0"
    });
    vector<string> res = A.reorderLogFiles(input);
    for (auto s : res) cout << s << endl;
    /* 
    "g1 act car"
    "a8 act zoo"
    "ab1 off key dog"
    "a1 9 2 3 1"
    "zo4 4 7"
    */ 
    return 0;
}