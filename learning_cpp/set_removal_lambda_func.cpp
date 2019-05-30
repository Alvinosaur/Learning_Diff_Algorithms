#include <iostream>
#include <set>
#include <iterator>
#include <string>
#include <functional>
#include <vector>
 
/*
 * Creating a generic function that will erase elements from container
 * while iterating if any given condition matches.
 *
 * It accepts following arguments
 *
 * 1.) Container i.e. set, list or vector
 * 2.) Iterator pointing to start of range
 * 3.) Iterator pointing to end of range
 * 4.) Callback to check if it needs to delete the current element
 *
 * It Iterates over the range and check if element needs to be deleted using passed checker callback.
 * If Yes then it deletes the element
 */
template <typename T, typename S>
void erase_if(T & group, S first, S last, std::function<bool (T)>checker)
{
	while(first != last) {
		if (checker(first)) {
			first = group.erase(first);
		}
		else first++;
	}
}


int main()
{
 
	typedef std::set<std::string>::iterator SetIter ;
 
	// Set Of String
	std::set<std::string> setOfStrs = {"Hi", "Hello", "is", "the", "at", "Hi", "is", "from", "that"};
 
	// Printing Set Contents
	std::copy(setOfStrs.begin(), setOfStrs.end(), std::ostream_iterator<std::string>(std::cout, ", "));
	std::cout<<std::endl;
 
	// Callback to check if size of string is greater than 2.
	std::function<bool (SetIter)> lambda = [](SetIter it) -> bool {
											return it->size() > 2;
										};
	// Remove all strings from set whose length is greater than 3.
	erase_if<>(setOfStrs, setOfStrs.begin(), setOfStrs.end(), lambda);
 
 
	// Printing Set Contents
	std::copy(setOfStrs.begin(), setOfStrs.end(), std::ostream_iterator<std::string>(std::cout, ", "));
	std::cout<<std::endl;
 
	return 0;
}