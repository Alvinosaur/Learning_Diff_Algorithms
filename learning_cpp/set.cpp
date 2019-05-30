#include<iostream>
#include<set>
#include<string>

// Sets are implemented as balanced binary search tree
int main()
{
 
	std::set<std::string> setOfNumbers;
 
	// Lets insert four elements
	setOfNumbers.insert("first");
	setOfNumbers.insert("second");
	setOfNumbers.insert("third");
	setOfNumbers.insert("first");
 
	// Iterate through all the elements in a set and display the value.
	for (std::set<std::string>::iterator it=setOfNumbers.begin(); it!=setOfNumbers.end(); ++it)
	    std::cout << ' ' << *it;
 
	std::cout<<std::endl;

	// Search for element in set using find member function
	std::set<std::string>::iterator it = setOfNumbers.find("first");
	if(it != setOfNumbers.end())
		std::cout<<"'first'  found"<<std::endl;
	else
		std::cout<<"'first' not found"<<std::endl;
 
 
	setOfNumbers.erase("third");
 
	// Iterate through all the elements in a set and display the value.
	for (std::set<std::string>::iterator it=setOfNumbers.begin(); it!=setOfNumbers.end(); ++it)
		    std::cout << ' ' << *it;
 
	std::cout<<std::endl;
	return 0;
}