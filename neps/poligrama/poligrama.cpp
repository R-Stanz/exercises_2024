#include <iostream>
#include <unordered_map>

using namespace std;

void print_sub_str(string& str, int& min_len);
int get_min_sub_str_len(string& str, unordered_map<char,int>& sub_str_chrs_count);
bool isnt_valid(string& str, unordered_map<char,int>& sub_str_chrs_count, int& min_len, char& last_invalid_chr);

int main() {

	int size;
	cin >> size;

	string str;
	cin >> str;

	unordered_map<char,int> sub_str_chrs_count;
	sub_str_chrs_count[str[0]] += 1;

	int min_sub_str_len = get_min_sub_str_len(str, sub_str_chrs_count);
	print_sub_str(str, min_sub_str_len);

	return 0;
}


void print_sub_str(string& str, int& min_len) {
	if (min_len > str.size()/2) {
		cout << "*" << endl;
	}
	else {
		for (int i = 0; i < min_len; i++) {
			cout << str[i];
		}
		cout << endl;
	}
}

int get_min_sub_str_len(string& str, unordered_map<char,int>& sub_str_chrs_count) {
	char last_invalid_chr = str[0];
	sub_str_chrs_count[last_invalid_chr] += 1;
	int min_len = 1;

	while (isnt_valid(str, sub_str_chrs_count, min_len, last_invalid_chr)) {
		while (true) {
			char& tmp_chr = str[min_len];
			sub_str_chrs_count[tmp_chr] += 1;

			if (str[min_len] == last_invalid_chr) {
				min_len += 1;
				break;
			}
			else {
				min_len += 1;
			}
		}
		
		while (sub_str_chrs_count.find(str[min_len]) == sub_str_chrs_count.end()) {
			sub_str_chrs_count[str[min_len]] += 1; 
			min_len += 1;
		}

	}
	return min_len;
}

bool isnt_valid(string& str, unordered_map<char,int>& sub_str_chrs_count, int& min_len, char& last_invalid_chr) {
	for (int i = min_len; i < str.size(); i += min_len) {
		unordered_map<char,int> tmp_sub_str_chrs_count;
		for (int u = 0; u < min_len; u++) {
			char& tmp_chr = str[i+u];

			if (sub_str_chrs_count.find(tmp_chr) == sub_str_chrs_count.end()) {
				last_invalid_chr = tmp_chr;
				return true;
			}
			
			tmp_sub_str_chrs_count[tmp_chr] += 1;
			if (tmp_sub_str_chrs_count[tmp_chr] > sub_str_chrs_count[tmp_chr]) {
				last_invalid_chr = tmp_chr;
				return true;
			}
		}
	}
	return false;
}
