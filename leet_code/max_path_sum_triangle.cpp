#include <cstdio>
#include <utility>

#define N 4

std::pair<int, int> find_max(int arr[N], int start=0, int end=N) {
    int max_val = -1, max_ind = 0;
    for (int i = start; i < end; i++) {
        if (i < 0 || i >= N) continue;
        if (arr[i] > max_val) {
            max_val = arr[i];
            max_ind = i;
        }
    }
    return std::make_pair(max_ind, max_val);
}

int max_path_sum(int tri[N][N]) {
    int sum = 0;
    int start = 0, end = N;
    for (int i = 0; i < N; i++) {
        std::pair<int, int>max_pair = find_max(tri[i], start, end);
        sum += max_pair.second;
        start = max_pair.first - 1;
        end = max_pair.first + 2;
    }
    return sum;
}

int main() {
    int tri[N][N] = {
        {3, 0, 0, 0},
        {7, 4, 0, 0},
        {2, 4, 6, 0},
        {8, 5, 9, 3}
    };
    printf("Sum: %d\n", max_path_sum(tri));
    return 0;
}