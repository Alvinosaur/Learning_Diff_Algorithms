#include <iostream>
#include <vector>
 
struct Sample
{
    Sample(){}
    Sample(const Sample & obj)
    {
        std::cout<<"Sample copy constructor"<<std::endl;
    }
};

int main()
{
    std::vector<Sample> vecOfInts;
 
    // capacity is how many elements can be stored before resizing
    // initially, capacity is 0
    // size is number of elements currently stored
    std::cout<<"Capacity :: "<<vecOfInts.capacity()<<std::endl;
    std::cout<<"Size :: "<<vecOfInts.size()<<std::endl;
    int capcity = vecOfInts.capacity();
    // fill up vector to full capacity, no resizng yet
    for(int i = 0; i < capcity + 1; i++)
        vecOfInts.push_back(Sample());
 
    std::cout<<"Capacity :: "<<vecOfInts.capacity()<<std::endl;
    std::cout<<"Size :: "<<vecOfInts.size()<<std::endl;
 
    // reiszing happens after first insertion
    // print out copy constructor capacity times
    for(int i = 0; i < capcity + 1; i++)
            vecOfInts.push_back(Sample());
 
    std::cout<<"Capacity :: "<<vecOfInts.capacity()<<std::endl;
    std::cout<<"Size :: "<<vecOfInts.size()<<std::endl;

    // Will have to resize
    vecOfInts.push_back(Sample());
 
    return 0;
}