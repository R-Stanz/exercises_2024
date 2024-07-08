#include <iostream>

using namespace std;

int find_min(int target_sum, int interval_ini, int interval_end);
int find_max(int target_sum, int interval_ini, int interval_end);
int digits_sum(int num);

int main() {
	int target_sum;
	cin >> target_sum;

	int interval_ini, interval_end;
	cin >> interval_ini >> interval_end;

	cout << find_min(target_sum, interval_ini, interval_end) << endl;
	cout << find_max(target_sum, interval_ini, interval_end) << endl;

	return 0;
}

int find_min(int target_sum, int interval_ini, int interval_end) {
	for (int i = interval_ini; i <= interval_end; i++) {
		if (digits_sum(i) == target_sum)
			return i;
	}
	return 0;
}

int find_max(int target_sum, int interval_ini, int interval_end) {
	for (int i = interval_end; i >= interval_ini; i--) {
		if (digits_sum(i) == target_sum)
			return i;
	}
	return 0;
}

int digits_sum(int num) {
	int sum = 0;
	while (num != 0) {
		sum += num % 10;
		num /= 10;
	}
	return sum;
}








