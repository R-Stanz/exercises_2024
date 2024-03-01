#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;

	int year, diff;
	for (int i = 0; i < n; i++){
		cin >> year;
		if (year < 2015) {
			diff = 2015 - year;
			cout << diff << " D.C.\n";
		}
		else {
			diff = year - 2014;
			cout << diff << " A.C.\n";
		}
	};

	return 0;
}
