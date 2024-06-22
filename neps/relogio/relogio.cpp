#include <iostream>

using namespace std;

int main() {

	int hour, min, sec;
	cin >> hour >> min >> sec;

	int delay;
	cin >> delay;


	sec += delay;
	min += sec / 60;
	hour += min / 60;

	sec %= 60;
	min %= 60;
	hour %= 24;

	cout << hour << endl << min << endl << sec << endl;

	return 0;
}
