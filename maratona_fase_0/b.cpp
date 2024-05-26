#include <iostream>
#include <map>
#include <unordered_set>

using namespace std;

int main() {
	int num_of_cities, num_of_stretches, num_visited_cities;
	cin >> num_of_cities >> num_of_stretches >> num_visited_cities;

	map<int, unordered_set<int>> cities_by_time;

	for (int i = 0; i < num_of_stretches; i++) {
		int city_a, city_b, time;
		cin >> city_a >> city_b >> time;

		cities_by_time[time].insert(city_a);
		cities_by_time[time].insert(city_b);
	}

	int smallest_time;
	for (auto &time_cities_pair : cities_by_time) {
		for (auto time_cities_prev_pair : cities_by_time) {
			if (time_cities_prev_pair == time_cities_pair)
				break;
			for (int i : time_cities_prev_pair.second)
				time_cities_pair.second.insert(i);
		}

		if (time_cities_pair.second.size() >= num_visited_cities) {
			smallest_time = time_cities_pair.first;
			break;
		}
	}

	cout << smallest_time << endl;

	return 0;
}
