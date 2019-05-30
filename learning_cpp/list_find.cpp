#include <iostream>
#include <list>
#include <string>
#include <algorithm>
 
// Generic type, T
template <typename T>

// Function to find generic element of type, T(defined above) in a list 
bool contains(std::list<T> & listOfElements, const T & element)
{
	// Find the iterator if element in list
	auto it = std::find(listOfElements.begin(), listOfElements.end(), element);
	//return if iterator points to end or not. It points to end then it means element
	// does not exists in list
	return it != listOfElements.end();
}

int main()
{
	std::list<std::string> listOfStrs({"is", "of", "the", "Hi", "Hello", "from" });
 
	// Check if an element exists in list
 
	// Create a list Iterator
	std::list<std::string>::iterator it;
 
	// Fetch the iterator of element with value 'the'
	it = std::find(listOfStrs.begin(), listOfStrs.end(), "the");
 
	// Check if iterator points to end or not
	if(it != listOfStrs.end())
	{
		// It does not point to end, it means element exists in list
		std::cout<<"'the' exists in list "<<std::endl;
	}
	else
	{
		// It points to end, it means element does not exists in list
		std::cout<<"'the' does not exists in list"<<std::endl;
	}

	bool result = contains(listOfStrs, std::string("the"));
		// Check if iterator points to end or not
	if(it != listOfStrs.end())
	{
		// It does not point to end, it means element exists in list
		std::cout<<"'the' exists in list "<<std::endl;
	}
	else
	{
		// It points to end, it means element does not exists in list
		std::cout<<"'the' does not exists in list"<<std::endl;
	}
 
}