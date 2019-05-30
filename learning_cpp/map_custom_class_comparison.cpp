#include <iostream>
#include <map>
#include <string>

class User {
	std::string id;
	std::string name;

public:
	User(std::string inputId, std::string inputName) :
	id(inputId), name(inputName)
	{}
	const std::string & getId() const {
		return id;
	}
	const std::string & getName() const {
		return name;
	}
	// set default comparison as comparing id
	bool operator<(const User & otherUser) const {
		return this->id < otherUser.id;
	}
};

void usingDefaultComparison() {
	std::cout << "Using Default Comparison" << std::endl;
	std::map<User, int> allUsers;
	allUsers.insert(std::make_pair<User, int>(User("1", "Alvin"), 1));

	// based on default comparison of id, this is a duplicate entry
	allUsers.insert(std::make_pair<User, int>(User("1", "Kevin"), 2));

	allUsers.insert(std::make_pair<User, int>(User("2", "Alvin"), 3));

	for (auto entry : allUsers) {
		std::cout << entry.first.getId() << entry.first.getName() << std::endl;
	}

}

// Compares names instead of id
struct anotherComparison {
	bool operator()(const User &left, const User &right) const {
		return left.getName() > right.getName(); 
	}
};

void usingCustomComparison() {
	std::cout << "Using Custom Comparison" << std::endl;
	std::map<User, int, anotherComparison> allUsers;
	allUsers.insert(std::make_pair<User, int>(User("1", "Alvin"), 1));

	// based on default comparison of id, this is a duplicate entry
	allUsers.insert(std::make_pair<User, int>(User("1", "Kevin"), 2));

	allUsers.insert(std::make_pair<User, int>(User("2", "Alvin"), 3));

	for (auto entry : allUsers) {
		std::cout << entry.first.getId() << entry.first.getName() << std::endl;
	}

}

int main() {
	usingDefaultComparison();
	usingCustomComparison();
	return 0;
}