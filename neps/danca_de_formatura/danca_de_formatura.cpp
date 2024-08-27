#include <iostream>
#include <vector>

using namespace std;

pair<vector<int>, vector<int>> dance(int numb_of_moves, int numb_of_rows, int numb_of_cols);
vector<int> get_range(int limit);
vector<vector<int>> get_positions(vector<int>& rows_positions, vector<int>& cols_positions);
void print(vector<vector<int>>& positions);

int main() {

	int numb_of_rows, numb_of_cols, numb_of_moves;
	cin >> numb_of_rows >> numb_of_cols >> numb_of_moves;

	pair<vector<int>, vector<int>> row_and_cols_final_positions = dance(numb_of_moves, numb_of_rows, numb_of_cols);

	vector<int>& rows_positions = row_and_cols_final_positions.first;
	vector<int>& cols_positions = row_and_cols_final_positions.second;


	vector<vector<int>> final_positions = get_positions(rows_positions, cols_positions);

	print(final_positions);

	return 0;
}

pair<vector<int>, vector<int>> dance(int numb_of_moves, int numb_of_rows, int numb_of_cols) {
	vector<int> rows_positions = get_range(numb_of_rows);
	vector<int> cols_positions = get_range(numb_of_cols);

	for (int i = 0; i < numb_of_moves; i++) {
		char option;
		cin >> option;

		int position_a, position_b;
		cin >> position_a >> position_b;

		if (option == 'L') {
			int tmp = rows_positions.at(position_a - 1);
			rows_positions.at(position_a - 1) = rows_positions.at(position_b - 1);
			rows_positions.at(position_b - 1) = tmp;
		}
		else {
			int tmp = cols_positions.at(position_a - 1);
			cols_positions.at(position_a - 1) = cols_positions.at(position_b - 1);
			cols_positions.at(position_b - 1) = tmp;
		}
	}

	return pair<vector<int>, vector<int>>{rows_positions, cols_positions};
}

vector<int> get_range(int limit) {
	vector<int> range;
	for (int i = 0; i < limit; i++) {
		range.push_back(i);
	}
	return range;
}

vector<vector<int>> get_positions(vector<int>& rows_positions, vector<int>& cols_positions) {
	vector<vector<int>> positions(rows_positions.size());
	for (int i = 0; i < rows_positions.size(); i++) {
		vector<int>& row = positions.at(i);
		int& initial_row = rows_positions.at(i);
		for (int& initial_col : cols_positions) {
			int initial_value = (initial_row * cols_positions.size()) + initial_col + 1;
			row.push_back(initial_value);
		}
	}
	return positions;
}

void print(vector<vector<int>>& positions) {
	for (vector<int>& row : positions) {
		for (int& val : row) {
			cout << val << " ";
		}
		cout << endl;
	}
}
