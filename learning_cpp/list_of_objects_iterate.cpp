#include <iostream>
#include <list>
#include <string>

struct Player 
{
	int id;
	std::string name;

	Player(int player_id, std::string player_name):
	id(player_id), name(player_name)
	{
	}
};

int main() {
std::list<Player> listofPlayers = { Player(22, "Sid"),
									Player(3, "Laura"),
									Player(43, "Riti"),
									Player(30,"Angel"),
									Player(2, "Laura")
									};

	//Create a reverse iterator of std::list
	// std::list<Player>::reverse_iterator revIt;
 
	// // Make iterate point to begining and incerement it one by one till it reaches the end of list.
	// for (revIt = listofPlayers.rbegin(); revIt != listofPlayers.rend(); revIt++)
	// {
	// 	// Access the object through iterator
	// 	int id = revIt->id;
	// 	std::string name = revIt->name;
 
	// 	//Print the contents
	// 	std::cout << id << " :: " << name << std::endl;
 
	// }
	for (auto it = listofPlayers.end(); it != listofPlayers.begin(); it--){
		// Access the object through iterator
		int id = it->id;
		std::string name = it->name;
 
		//Print the contents
		std::cout << id << " :: " << name << std::endl;
	}

	return 0;
}