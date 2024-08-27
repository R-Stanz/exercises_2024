// Time Limit Exceeded
#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>>  get_initial_positions(int numb_of_rows, int numb_of_cols);
vector<vector<int>>  dance(int numb_of_paces, vector<vector<int>>& positions);
void swap_cols(vector<vector<int>>& positions, int col_a, int col_b);
void print(vector<vector<int>>& positions);


int main() {

	int numb_of_rows, numb_of_cols, numb_of_paces;
	cin >> numb_of_rows >> numb_of_cols >> numb_of_paces;

	vector<vector<int>>  initial_positions = get_initial_positions(numb_of_rows, numb_of_cols);
	vector<vector<int>>  ending_positions =  dance(numb_of_paces, initial_positions);

	print(ending_positions);

	return 0;
}


vector<vector<int>> get_initial_positions(int numb_of_rows, int numb_of_cols) {
	vector<vector<int>> positions(numb_of_rows, vector<int>(numb_of_cols));
	int count = 1;
	for (vector<int>& row : positions) {
		for (int& i : row) {
			i = count;
			count++;
		}
	}
	return positions;
}


vector<vector<int>> dance(int numb_of_paces, vector<vector<int>>& positions) {
	if (numb_of_paces == 0) {
		return positions;
	}
	char option;
	cin >> option;

	int position_a, position_b;
	cin >> position_a >> position_b;

	if (option == 'L') {
		vector<int>& row_a = positions.at(position_a - 1);
		vector<int>& row_b = positions.at(position_b - 1);
		
		row_a.swap(row_b);
	}
	else {
		swap_cols(positions, position_a - 1, position_b - 1);
	}

	return dance(numb_of_paces-1, positions);
}

void swap_cols(vector<vector<int>>& positions, int col_a, int col_b) {
	for (vector<int>& row : positions) {
		int tmp = row.at(col_a);
		row.at(col_a) = row.at(col_b);
		row.at(col_b) = tmp;
	}
}

void print(vector<vector<int>>& positions) {
	for (vector<int>& row : positions) {
		for (int i : row) {
			cout << i << " ";
		}
		cout << endl;
	}
}
