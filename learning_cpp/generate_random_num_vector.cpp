#include <iostream>
#include <vector>
#include <algorithm>

int main(){
	std::vector<int> v;
	v.reserve(50);
	std::generate(v.begin(), v.end(), [](){return rand() % 100 ;} );
	for (auto it = v.begin(); it != v.end(); it++) {
	std::cout << *it << ", ";
	}
	// std::copy(v.begin(), v.end(), 
	// 	std::ostream_iterator<int>(std::cout, " "));
	std::cout << std::endl;
	return 0;
}