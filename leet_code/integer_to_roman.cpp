#include <string>
#include <map>
#include <iostream>
#include <cmath>

using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        string result;
        
        map<int, string> digits_to_roman = {
            {9, "IX"}, {8, "VIII"}, {7, "VII"}, {6, "VI"}, {10, "X"},
            {5, "V"}, {4, "IV"}, {3, "III"}, {2, "II"}, {1, "I"},
            {40, "XL"}, {50, "L"}, {90, "XC"}, {100, "C"},
            {400, "CD"}, {500, "D"}, {900, "CM"}, {1000, "M"}
        };
        int exp = 0;
        while (num > 0) {
            // start from low numbers and go higher
            int digit = (num % 10) * pow(10, exp);
            num /= 10;
            exp++;

            auto it = digits_to_roman.find(digit);

            cout << digit << endl;
            if (it == digits_to_roman.end()) {
                if (digit == 0) continue;
                string sub_res = "";
                auto it_sub = digits_to_roman.rbegin();
                while (digit > 0) {
                    if (digit >= it_sub->first) {
                                            cout << it_sub->first << endl;
                        digit -= it_sub->first;
                        sub_res += it_sub->second;
                    }
                    else it_sub++;
                }
                result.insert(0, sub_res);
                
                continue;
            }

            result.insert(0, it->second);

        }
        return result;
    }
};

int main() {
    Solution a = Solution();
    cout << a.intToRoman(1994) << endl;
}