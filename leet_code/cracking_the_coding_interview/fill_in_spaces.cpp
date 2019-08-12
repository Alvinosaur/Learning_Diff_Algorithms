#include <string>

using namespace std;

string fill_spaces(string s) {
    string res;
    res.reserve(s.size());
    for (int i = 0; i < s.size(); i++) {
        if (i == 0) {res[i] = s[i]; res[i+1] = 1; }
        else {
            char prev = res[res.size()-2];
            if (prev == s[i]) res[res.size()-1]++;
            else {
                res += s[i]; 
                res +=
        }
    }
}

