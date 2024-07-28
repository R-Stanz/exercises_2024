#include <iostream>
#include <set>

using namespace std;

bool has_rectangle(set<int>& circle_positions, int circle_size);

int main() {
	int numb_of_points;
	cin >> numb_of_points;

	set<int> circle_positions;
	int circle_size = 0;
	circle_positions.insert(circle_size);
	for (int i = 0; i < numb_of_points; i++) {
		int increment;
		cin >> increment;

		circle_size += increment;
		if (i < numb_of_points - 1) {
			circle_positions.insert(circle_size);
		}
	}

	if (has_rectangle(circle_positions, circle_size)) {
		cout << "S" << endl;
	}
	else {
		cout << "N" << endl;
	}

	return 0;
}

bool has_rectangle(set<int>& circle_positions, int circle_size) {
	int has_half_counterpart_count = 0;
	for (int position : circle_positions) {
		if ((position >= circle_size / 2) or (circle_size % 2 != 0)) {
			return false;
		}

		int counterpart = position + circle_size / 2;
		if (circle_positions.find(counterpart) != circle_positions.end()) {
			if (has_half_counterpart_count >= 1) {
				return true;
			}
			has_half_counterpart_count += 1;
		}
	}
	return false;
}
