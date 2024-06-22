#include <iostream>

using namespace std;

int main() {

	int left_fingers;
	int right_fingers;
	cin >> left_fingers >> right_fingers;

	if (left_fingers > right_fingers) {
		cout << left_fingers + right_fingers << endl;
	}
	else {
		cout << 2 * (right_fingers - left_fingers) << endl;
	}

	return 0;
}
