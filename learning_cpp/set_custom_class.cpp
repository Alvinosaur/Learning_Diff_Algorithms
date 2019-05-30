#include <iostream>
#include <set>
#include <vector>
#include <string>

class Message {
public:
	std::string msgContent;
	std::string sentBy;
	std::string sentTo;

	Message(std::string _sentBy, std::string recBy, std::string msg) :
		msgContent(msg), sentBy(_sentBy), sentTo(recBy)
		{}

	bool operator< (const Message & msgObj) const {
		std::string leftStr = this->msgContent + this->sentBy + this->sentTo;
		std::string rightStr = (
			msgObj.msgContent + msgObj.sentBy + msgObj.sentTo);
		return leftStr < rightStr;
	}

	friend std::ostream& operator<<(std::ostream& os, const Message& obj);

};
std::ostream& operator<<(std::ostream& os, const Message& obj) {
	os << obj.sentBy << " :: " << obj.sentTo << " :: " << obj.msgContent;
	os << std::endl;
	return os;
}

int main() {
	std::set<Message> setOfMsgs;
 
	Message msg1("user_1", "Hello", "user_2");
	Message msg2("user_1", "Hello", "user_3");
	Message msg3("user_3", "Hello", "user_1");
	// A Duplicate Message
	Message msg4("user_1", "Hello", "user_3");
 
	setOfMsgs.insert(msg1);
	setOfMsgs.insert(msg2);
	setOfMsgs.insert(msg3);
	setOfMsgs.insert(msg4);
 
	// msg4 will not get inserted because its duplicate as per the current operator < implementation.
 
	// Iterate through all the elements in a set and display the value.
	for (auto elem : setOfMsgs) {
		std::cout << elem;
	}

	// Checking of size is must
	if(setOfMsgs.size() > 2)
	{
		std::set<Message>::iterator it = std::next(setOfMsgs.begin(), 2);
		std::cout<<"2nd Element in set = "<<*it<<std::endl;
	}

	// Can also insert using iterator range
	std::vector<std::string> vecOfStrs = {"Hi", "Hello", "is", "the", "at", "Hi", "is"};
	std::set<std::string> setOfStrs;
	setOfStrs.insert(vecOfStrs.begin(), vecOfStrs.end());

	// Can also insert using initializer list 
	setOfStrs.insert({"Hi", "Hello", "is", "the", "at", "Hi", "is"});
 
	return 0;
}