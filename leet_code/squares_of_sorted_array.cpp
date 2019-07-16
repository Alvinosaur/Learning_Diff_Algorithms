#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

vector<int> sortedSquares(vector<int>& A) {
    int N = A.size();
    vector<int> result(N);  
    // NOTE: reserve() doesn't actually set size, just sets internal max size 
    // so push_back doesn't dynamically reallocate
    int i = 0, j = N - 1;
    for (int p = N-1; p >= 0; p--) {
        if (abs(A[i]) > abs(A[j])) {
          result[p] = A[i] * A[i];
          i++;
        }
        else {
          result[p] = A[j] * A[j];
          j--;
        }
    }
    return result;
}

int main() {
  vector<int> a{-4, -1, 0, 2, 3};
  vector<int> result;
  result = sortedSquares(a);
  for (int it : a) cout << it << endl;
  return 0;
}