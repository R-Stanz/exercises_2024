#include <iostream>

using namespace std;

void build_ls(int* ls, int ls_size);
//int count_operations(int* ls, int left_marker, int right_marker, int sum = 0); Recursive Aproach
int count_operations(int* ls, int left_marker, int right_marker);

int main() {
	int ls_size;
	cin >> ls_size;

	int ls[ls_size];

	build_ls(ls, ls_size);

	cout << count_operations(ls, 0, ls_size - 1) << endl;

	return 0;
}

void build_ls(int* ls, int ls_size) {
	for (int i = 0; i < ls_size; i++) {
		cin >> ls[i];
	}
}

/* Test Cases Too Big Too Use Recursion
 * (Segmentation Fault, Stack Over Flow)

int count_operations(int* ls, int left_marker, int right_marker, int sum) {
	if (left_marker >= right_marker) {
		return sum;
	}

	if (ls[left_marker] == ls[right_marker]) {
		return count_operations(ls, left_marker + 1, right_marker - 1, sum);
	}
	else if (ls[left_marker] < ls[right_marker]) {
		ls[left_marker + 1] += ls[left_marker];
		return count_operations(ls, left_marker + 1, right_marker, sum + 1);
	}

	else {
		ls[right_marker - 1] += ls[right_marker];
		return count_operations(ls, left_marker, right_marker - 1, sum + 1);
	}
}
*/

int count_operations(int* ls, int left_marker, int right_marker) {
	int sum = 0;
	while (left_marker < right_marker) {

		if (ls[left_marker] == ls[right_marker]) {
			left_marker += 1;
			right_marker -= 1;
		}
		else if (ls[left_marker] < ls[right_marker]) {
			ls[left_marker + 1] += ls[left_marker];
			left_marker += 1;
			sum += 1;
		}

		else {
			ls[right_marker - 1] += ls[right_marker];
			right_marker -= 1;
			sum += 1;
		}
	}
	return sum;
}
