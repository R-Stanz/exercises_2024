#include <iostream>

using namespace std;

bool check_first_3_chr(string& plate);
bool check_brasil(string& plate);
bool check_mercosul(string& plate);
bool is_digit(char chr);
bool is_valid_letter(char chr);

int main() {

	string plate;
	cin >> plate;

	if (not check_first_3_chr(plate)) {
		cout << 0 << endl;
		return 0;
	}

	if ((plate.length() == 8) and check_brasil(plate)) {
		cout << 1 << endl;
	}
	else if ((plate.length() == 7) and check_mercosul(plate)) {
		cout << 2 << endl;
	}
	else {
		cout << 0 << endl;
	}

	return 0;
}

bool check_first_3_chr(string& plate) {
	if (plate.length() < 7) {
		return false;
	}

	for (int i = 0; i < 3; i++) {
		if (not is_valid_letter(plate[i])) {
			return false;
		}
	}

	return true;
}

bool check_brasil(string& plate) {
	int i = 3;
	if (plate[i] != '-') {
		return false;
	}

	i += 1;

	for (i; i < 8; i++) {
		if (not is_digit(plate[i])) {
			return false;
		}
	}

	return true;
}

bool check_mercosul(string& plate) {
	int i = 3;
	if (not is_digit(plate[i])) {
		return false;
	}
	i += 1;

	if (not is_valid_letter(plate[i])) {
		return false;
	}
	i += 1;

	for (i; i < 7; i++) {
		if (not is_digit(plate[i])) {
			return false;
		}
	}

	return true;
}

bool is_digit(char chr) {
	if ((chr >= '0') and (chr <= '9')) {
		return true;
	}

	return false;
}

bool is_valid_letter(char chr) {
	if ((chr >= (int) 'A') and (chr <= (int) 'Z')) {
		return true;
	}

	return false;
}
