#include <iostream>
#include <vector>


int basics() {
	// Like a dynamically-allocated array, ordered
	std::vector<int> v;

	for (int i = 0; i < 5; i++) {
		// O(1) append to end of vector
		v.push_back(i);
	}

	// iterator is a pointer to item in vector
	// begin() and end() return ptrs as well
	std::vector<int>::iterator it = v.begin();
	// auto it = v.begin();
	while(it != v.end()) {
		std::cout << *it << ", ";
		// int ptr, so increment just increments 
		it++;
	}

	std::cout << std::endl;

	for (int i = 0; i < v.size(); i++) {
		std::cout << v[i] << ", ";
	}

	std::cout << std::endl;

	return 0;
}

int diff_inits() {
	// Can init with initial size, values all set to 0
	std::vector<int> v(5);

	// Can init with chosen elements
	std::vector<std::string> v2(5, "Hi");
	for(std::string str : v2)
		std::cout<<str<<std::endl;

	// Can init vector using an existing array
	std::string arr[] = {"first", "second", "third", "fourth"};
	// pass in ptr(iterator) to start of array and where u want it to end
	std::vector<std::string> v3(arr, arr + 4);
	for(std::string str : v3)
		std::cout<<str<<std::endl;

	std::list<std::string> l;
	l.push_back("1");
	l.push_back("2");
	l.push_back("3");
	std::vector<std::string> v4(l.begin(), l.end());

	// Can init with another vecotr
	std::vector<std::string> v5(v4);

	return 0;
}

int main() {
	basics();
	diff_inits();
	return 0;
}