#include <iostream>
#include <vector>

// O(N^2)
void naive_removal(std::vector<int> &V, int elem) {
	auto it = V.begin();
	while (it != V.end()) {
		if (*it == elem) {
			it = V.erase(it);
		}
		else it++;
	}
}

// O(N)
void linear_removal(std::vector<int> &V, int elem) {
	// remove loops through and moves all non-matching elem to front
	// returns iterator to new end, which is start of all matching elem
	V.erase(std::remove(V.begin(), V.end(), elem), V.end());
}

int main() {
	std::vector<int> V({1, 2, 5, 3, 5 ,7, 5, 9, 5});
	// naive_removal(V, 5);
	linear_removal(V, 5);

	auto it = V.begin();
	while (it != V.end()) {
		std::cout << *it << ", ";
		it++;
	}
	std::cout << std::endl;
	return 0;

}