#include <iostream>
#include <vector>

using namespace std;

void build_cells_matrix(vector<vector<bool>>& cells);
void new_turn(vector<vector<bool>>& cells);
void apply_rules(vector<vector<bool>>& cells, vector<vector<bool>>& next_cells, int& line, int& col);
int count_alive_neighbors(vector<vector<bool>>& cells, int& line, int& col);
int alive_count_by_line(vector<vector<bool>>& cells, int line, int& col);
void print(vector<vector<bool>>& cells);

int main() {

	int dim, turns;
	cin >> dim >> turns;

	vector<vector<bool>> cells(dim);

	build_cells_matrix(cells);

	for (int i = 0; i < turns; i++) {
		new_turn(cells);
	}

	print(cells);

	return 0;
}

void build_cells_matrix(vector<vector<bool>>& cells) {
	for (vector<bool>& line : cells) {
		string cell_line_str;
		cin >> cell_line_str;
		for (char c : cell_line_str) {
			if (c == '1') {
				line.push_back(true);
			}
			else {
				line.push_back(false);
			}
		}
	}
}

void new_turn(vector<vector<bool>>& cells) {
	vector<vector<bool>> next_cells;
	next_cells.insert(next_cells.end(), cells.begin(), cells.end());

	for (int line = 0; line < cells.size(); line++) {
		for (int col = 0; col < cells.size(); col++) {
			apply_rules(cells, next_cells, line, col);
		}
	}
	cells.clear();
	cells.insert(cells.end(), next_cells.begin(), next_cells.end());
}

void apply_rules(vector<vector<bool>>& cells, vector<vector<bool>>& next_cells, int& line, int& col) {
	int alive_neighbors_count = count_alive_neighbors(cells, line, col);

	bool current_cell_status = cells.at(line).at(col);
	if (current_cell_status) {
		if ((alive_neighbors_count < 2) or (alive_neighbors_count > 3)) {
			next_cells.at(line).at(col) = false;
		}
	}
	else {
		if (alive_neighbors_count == 3) {
			next_cells.at(line).at(col) = true;
		}
		else {
			next_cells.at(line).at(col) = false;
		}
	}
}

int count_alive_neighbors(vector<vector<bool>>& cells, int& line, int& col) {

	int alive_neighbors_count = alive_count_by_line(cells, line+1, col);
	alive_neighbors_count += alive_count_by_line(cells, line, col);
	alive_neighbors_count += alive_count_by_line(cells, line-1, col);

	if (cells.at(line).at(col)) {
		alive_neighbors_count -= 1;
	}

	return alive_neighbors_count;
}


int alive_count_by_line(vector<vector<bool>>& cells, int line, int& col) {
	if ((line >= cells.size()) or (line < 0)) {
		return 0;
	}

	int count = 0;

	if ((col - 1 >= 0) and cells.at(line).at(col-1)) {
		count += 1;
	}
	if (cells.at(line).at(col)) {
		count += 1;
	}
	if ((col + 1 < cells.size()) and cells.at(line).at(col+1)) {
		count += 1;
	}
	return count;
}

void print(vector<vector<bool>>& cells) {
	cout << endl;
	for (vector<bool>& line : cells) {
		for (bool cell_status : line) {
			cout << cell_status;
		}
		cout << endl;
	}
}
