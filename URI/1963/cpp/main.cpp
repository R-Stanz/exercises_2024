#include <stdio.h>
#include <iomanip>
#include <iostream>

using namespace std;

int main() {
	
	double a, b;
	cin >> a >> b;

	double result = 100 * (b-a)/a;
	cout << fixed << setprecision(2) << result << "%\n";

	return 0;
}
