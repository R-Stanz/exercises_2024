#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {

	int queue_size;
	cin >> queue_size;
	vector<int> queue_with_ids;

	for (int i = 0; i < queue_size; i++) {
		int new_id;
		cin >> new_id;
		queue_with_ids.push_back(new_id);
	}

	int reduce_queue;
	cin >> reduce_queue;
	unordered_set<int> exited_ids;
	for (int i = 0; i < reduce_queue; i++) {
		int id;
		cin >> id;
		exited_ids.insert(id);
	}

	bool printed_first_id = false;
	for (int i = 0; i < queue_size; i++) {
		int id = queue_with_ids.at(i);
		// if (not exited_ids.contains(id)) {
		if (not (exited_ids.find(id) != exited_ids.end())) {
			if (printed_first_id)
				cout << " ";
			else
				printed_first_id = not printed_first_id;
			cout << id;
		}
	}
	cout << endl;
	return 0;
}
