#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {

	vector<int> players_lvls(4);
	for (int& player_lvl : players_lvls) {
		cin >> player_lvl;
	}
	sort(players_lvls.begin(), players_lvls.end());

	int team_1 = players_lvls.at(0) + players_lvls.at(3);
	int team_2 = players_lvls.at(1) + players_lvls.at(2);
	int diff = team_1 - team_2;

	cout << diff << endl;

	return 0;
}
