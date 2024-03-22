#include <iostream>
#include <vector>

using namespace std;

bool is_linked(int city, vector<int> links_list);

int main() {
	int n,m;

	cin >> n >> m;

	vector<vector<int>> cities_links;
	for (int i = 0; i < n; i++)
		cities_links.push_back({});

	vector<int> linked_cities;

	for (int i = 0; i < m; i++) {
		int city_a, city_b;
		cin >> city_a >> city_b;

		if ((city_a == city_b) || (city_a > n) || (city_b > n)) {
			cout << "-1" << endl;
			return 0;
		}

		if (! is_linked(city_b, cities_links.at(city_a-1)) ||
			(! is_linked(city_a, cities_links.at(city_b-1)))) {

			cities_links.at(city_a-1).push_back(city_b);
			cities_links.at(city_b-1).push_back(city_a);
		}

		if (! is_linked(city_a, linked_cities)) {
			linked_cities.push_back(city_a);
		}

		if (! is_linked(city_b, linked_cities)) {
			linked_cities.push_back(city_b);
		}
	}

	for (int i = 0; i < cities_links.size(); i++) {

		vector<int> city_links(cities_links.at(i));

		if ((city_links.size() < linked_cities.size() - 1) &&
			(city_links.size() > 0)) {

			for (int city : linked_cities) {
				if (! is_linked(city, city_links) && (city != i+1)) {
					cout << city << " " << i+1 << endl;
					return 0;
				}
			}
		}
	}

	cout << "-1" << endl;
	return 0;
}


bool is_linked(int city, vector<int> links_list) {
	for (int linked_city : links_list) {
		if (city == linked_city) {
			return true;
		}
	}
	return false;
}
