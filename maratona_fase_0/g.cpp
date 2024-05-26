#include <iostream>
#include <map>
#include <queue>

using namespace std;

int main() {

	int num_stops, autonomy;
	cin >> num_stops >> autonomy;

	queue<int> coord_queue;
	for (int i = 0; i < num_stops; i++) {
		int new_coord;
		cin >> new_coord;
		coord_queue.push(new_coord);
	}

	map<int,int> stores;
	while (true) {
		int store_stock;
		cin >> store_stock;
		stores[coord_queue.front()] = store_stock;
		if (coord_queue.size() == 1) {
			if (coord_queue.front() <= autonomy) {
				cout << "0" << endl;
				return 0;
			}
			break;
		}
		coord_queue.pop();
	}

	auto last_store = stores.end();
	int stop_count = 0;
	for (auto tmp_store = stores.begin(); tmp_store != stores.end(); tmp_store++) {
		if (autonomy - tmp_store->first < 0) {
			stop_count++;
			tmp_store = prev(tmp_store);
			if (tmp_store == stores.begin()) {
				cout << "-1" << endl;
				return 0;
			}
			if (last_store == tmp_store) {
				stop_count--;
				tmp_store = prev(tmp_store);
			}
			autonomy = tmp_store->second + tmp_store->first;
			tmp_store++;
		}
	}
	cout << stop_count << endl;
	return 0;
}
