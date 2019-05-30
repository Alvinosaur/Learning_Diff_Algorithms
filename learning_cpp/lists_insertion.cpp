#include <iostream>
#include <list>

int main() {
// []
std::list<int> listOfNumbers;

// [5, 6]
listOfNumbers.push_back(5);
listOfNumbers.push_back(6);

// [1, 2, 5, 6]
listOfNumbers.push_front(2);
listOfNumbers.push_front(1);

// it points at 1
auto it = listOfNumbers.begin();

// it points at 5
it++; it++;

// insert item before 5
listOfNumbers.insert(it, 0);

std::cout << "list: ";

for (it = listOfNumbers.begin(); it != listOfNumbers.end(); it++){
	std::cout << *it;
}

std::cout << std::endl;
}