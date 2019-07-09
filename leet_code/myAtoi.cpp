#include <iostream>
#include <cmath>
#include <stdint.h>
#include <cstring>

using namespace std;

int myAtoi(string str) {
    for (auto it = str.begin(); it != str.end(); it++) {
    bool is_negative;
    uint32_t result;
        if (strncmp(*it, " ", 1) == 0) continue;
        else if (strncmp(*it, "-", 1) == 0) is_negative = true;
        else {
            try {
                int digit = *it - '0';
                // Not a number
                if (digit > 10 || digit < 0) {
                    return 0;
                }
                // Deal with overflow here
                if (is_negative) {
                    if (result > (INT_MAX - digit + 1) / 10)
                        return INT_MIN;
                }
                else {
                    if (result > (INT_MAX - digit) / 10)
                        return INT_MAX;
                }
                result = result * 10 + (uint32_t)digit;
            }
            except {
                return 0;
            }
        }
    }
    if (is_negative) return -1 * result;
    else return result;
}

int main() {
    std::cout << myAtoi(std::string("42")) << std::endl;
    std::cout << myAtoi(std::string("42")) << std::endl;
    return 0;
}