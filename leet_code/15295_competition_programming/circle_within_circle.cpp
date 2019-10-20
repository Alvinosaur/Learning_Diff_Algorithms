#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main(int arg, char** argv)
{
    /* Naive 2: sort input list of numbers, we know that every even index
    radius is outer radius of red part, the previous index radius is bound */
    // USE long double for greater precision
	int N;
    cin >> N;
    uint32_t radii[N];
	for (int i = 0; i < N; ++i) {
		cin >> radii[i];
	}
    sort(radii, radii+N);
    uint32_t area = radii[0] * radii[0];
    for (int i = 2; i < N; i+=2) {
        area += (radii[i] * radii[i]) - (radii[i-1] * radii[i-1]);
    }

    cout << (M_PI * area) << endl;
	return 0;
}