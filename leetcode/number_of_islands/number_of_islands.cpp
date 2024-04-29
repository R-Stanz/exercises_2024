class Solution {
public:
	struct hashFunction { 
		size_t operator()(const pair<int,int> &x) 
		const {
			return x.first ^ x.second;
		} 
	};

	void fill_earth_coord_set(vector<vector<char>>& grid, unordered_set<pair<int,int>, hashFunction>& earth_coord_set) {
		int last_line = grid.size() - 1;
		int last_col = grid.at(0).size() - 1;

		for (int line = 0; line <= last_line; line++) {
			for (int col = 0; col <= last_col; col++) {
				if (grid.at(line).at(col) == '1') {
					pair<int,int> new_coord = make_pair(line, col);
					earth_coord_set.insert(new_coord);
				}
			}
		}
	}

	int numIslands(vector<vector<char>>& grid) {
		int last_line = grid.size() - 1;
		int last_col = grid.at(0).size() - 1;

		unordered_set<pair<int,int>, hashFunction> earth_coord_set;
		fill_earth_coord_set(grid, earth_coord_set);

		int islands = 0;
		while (not earth_coord_set.empty()) {
			++islands;

			pair<int,int> new_earth_coord;
			for (auto coord : earth_coord_set) {
				new_earth_coord = coord;
				earth_coord_set.erase(coord);
				break;
			}

			if (earth_coord_set.empty())
				return islands;

			vector<pair<int,int>> new_earth_coords{new_earth_coord};
			while (not new_earth_coords.empty()) {
				pair<int,int> new_coord = new_earth_coords.at(new_earth_coords.size() - 1);
				new_earth_coords.pop_back();
				
				int line = new_coord.first;
				int col = new_coord.second;

				pair<int,int> upper_neighbor{line + 1, col};
				if ((line + 1 <= last_line) and (earth_coord_set.contains(upper_neighbor))) {
					new_earth_coords.push_back(upper_neighbor);
					earth_coord_set.erase(upper_neighbor);
				}

				pair<int,int> bottom_neighbor{line - 1, col};
				if ((line - 1 >= 0) and (earth_coord_set.contains(bottom_neighbor))) {
					new_earth_coords.push_back(bottom_neighbor);
					earth_coord_set.erase(bottom_neighbor);
				}

				pair<int,int> left_neighbor{line, col - 1};
				if ((line >= 0) and (earth_coord_set.contains(left_neighbor))) {
					new_earth_coords.push_back(left_neighbor);
					earth_coord_set.erase(left_neighbor);
				}

				pair<int,int> right_neighbor{line, col + 1};
				if ((col + 1 <= last_col) and (earth_coord_set.contains(right_neighbor))) {
					new_earth_coords.push_back(right_neighbor);
					earth_coord_set.erase(right_neighbor);
				}
			}
		}
		return islands;
	}
};
