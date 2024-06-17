#include <iostream>

using namespace std;

int hash_a_line(int line, string str, int pos = 0, int hash = 0);

int main() {
	
	int test_cases;
	cin >> test_cases;
	int results[test_cases]{0};

	for (int k = 0; k < test_cases; k++) {
		int numb_of_lines;
		cin >> numb_of_lines;
		for (int line = 0; line < numb_of_lines; line++) {
			string str;
			cin >> str;

			results[k] += hash_a_line(line, str);
		}
	}

	for (int i : results) {
		cout << i << endl;
	}

	return 0;
}


int hash_a_line(int line, string str, int pos, int hash) {
	if (str.length() > pos) {
		hash += (int) str[pos] - (int) 'A' + line + pos;
		return hash_a_line(line, str, pos + 1, hash);
	}
	return hash;
}
