
#include <iostream>
#include <deque>
 
int main()
{
    std::deque<int> dequeObj;
 
    dequeObj.push_back(5);
    dequeObj.push_back(6);
 
    for(int i = 0; i< dequeObj.size(); i++)
        std::cout<<dequeObj[i]<<" ";
    std::cout<<std::endl;
 
    dequeObj.push_front(4);
    dequeObj.push_front(3);
 
    for(int i = 0; i< dequeObj.size(); i++)
            std::cout<<dequeObj[i]<<" ";
    std::cout<<std::endl;
 
    dequeObj.pop_back();
 
    for(int i = 0; i< dequeObj.size(); i++)
            std::cout<<dequeObj[i]<<" ";
    std::cout<<std::endl;
 
    dequeObj.pop_front();
 
    for(int i = 0; i< dequeObj.size(); i++)
                std::cout<<dequeObj[i]<<" ";
    std::cout<<std::endl;
    return 0;
}