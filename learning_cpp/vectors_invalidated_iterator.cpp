#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>
 
int main()
{
    std::vector<int> vecArr;
    for(int i = 1; i <= 10; i++)
        vecArr.push_back(i);
 
    for(auto it = vecArr.begin(); it != vecArr.end(); it++)
        std::cout<<(*it)<<"  ";
 
    std::cout<<std::endl;
 
    // Erase and element with value 5.
    auto it = std::find(vecArr.begin(), vecArr.end(), 5);
    if(it != vecArr.end()) {
        vecArr.erase(it);
		// Solution:
		//it = vecArr.erase(it);
	}
		
 
    // Now iterator 'it' is invalidated because it still points to
    // old location, which has been deleted. So, if you will try to
    // do the use the same iterator then it can show undefined
    // behavior.
 
    for(; it != vecArr.end(); it++)   // Unpredicted Behavior
        std::cout<<(*it)<<"  ";          // Unpredicted Behavior
 
    return 0;
}