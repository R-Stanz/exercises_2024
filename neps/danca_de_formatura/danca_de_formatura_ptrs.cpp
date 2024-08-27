// Time limit exceeded
#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>>  get_initial_positions(int numb_of_rows, int numb_of_cols);
vector<vector<int*>> get_positions_by_cols(vector<vector<int>>& positions, int numb_of_rows, int numb_of_cols);
vector<vector<int>>  dance(int numb_of_paces, vector<vector<int>>& initial_positions, vector<vector<int*>>& initial_positions_by_cols);
void swap_cols(vector<int*>& col_a, vector<int*>& col_b);
void print(vector<vector<int>>& positions);


int main() {

	int numb_of_rows, numb_of_cols, numb_of_paces;
	cin >> numb_of_rows >> numb_of_cols >> numb_of_paces;

	vector<vector<int>>  initial_positions = get_initial_positions(numb_of_rows, numb_of_cols);
	vector<vector<int*>> positions_by_cols = get_positions_by_cols(initial_positions, numb_of_rows, numb_of_cols);
	vector<vector<int>>  ending_positions =  dance(numb_of_paces, initial_positions, positions_by_cols);

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

vector<vector<int*>> get_positions_by_cols(vector<vector<int>>& positions, int numb_of_rows, int numb_of_cols) {
	vector<vector<int*>> positions_by_cols(numb_of_cols);

	for (int c = 0; c < numb_of_cols; c++) {
		
		vector<int*>& col = positions_by_cols.at(c);
		
		for (int r = 0; r < numb_of_rows; r++) {
			int* val = &(positions.at(r).at(c));
			col.push_back(val);
		}
	}
	return positions_by_cols;
}

vector<vector<int>> dance(int numb_of_paces, vector<vector<int>>& positions, vector<vector<int*>>& positions_by_cols) {
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
		vector<int*>& col_a = positions_by_cols.at(position_a - 1);
		vector<int*>& col_b = positions_by_cols.at(position_b - 1);
		
		swap_cols(col_a, col_b);
	}

	return dance(numb_of_paces-1, positions, positions_by_cols);
}

void swap_cols(vector<int*>& col_a, vector<int*>& col_b) {
	for (int i = 0; i < col_a.size(); i++) {
		int tmp = *(col_a.at(i));
		*(col_a.at(i)) = *(col_b.at(i));
		*(col_b.at(i)) = tmp;
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
