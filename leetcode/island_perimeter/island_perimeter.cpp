class Solution {
public:
	int islandPerimeter(vector<vector<int>>& grid) {
		int perimeter = 0;
		int row_index_max_limit = grid.size() - 1;
		for (int row_index = 0; row_index <= row_index_max_limit; row_index++) {

			vector<int>* row = &grid.at(row_index);
			int col_max_limit = row->size() - 1;
			for (int col = 0; col <= col_max_limit; col++) {
				int point = row->at(col);
				if (point == 1) {

					if (row_index == 0)
						perimeter += 1;
					if (row_index == row_index_max_limit)
						perimeter += 1;
					if (col == 0)
						perimeter += 1;
					if (col == col_max_limit)
						perimeter += 1;

					if ((row_index - 1 >= 0) && (grid.at(row_index - 1).at(col) == 0))
						perimeter += 1;
					if ((row_index + 1 <= row_index_max_limit) && (grid.at(row_index + 1).at(col) == 0))
						perimeter += 1;
					if ((col - 1 >= 0) && (row->at(col - 1) == 0))
						perimeter += 1;
					if ((col + 1 <= col_max_limit) && (row->at(col + 1) == 0))
						perimeter += 1;
				}
			}
		}
		return perimeter;
	}
};
