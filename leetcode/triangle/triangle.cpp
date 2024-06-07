class Solution {
public:
	int minimumTotal(vector<vector<int>>& triangle) {

		for (int lvl = triangle.size() - 1; lvl > 0; lvl--) {
			for (int marker = 0; marker < triangle[lvl-1].size(); marker++) {
				
				int min_in_pair = triangle.at(lvl).at(marker);
				if (triangle.at(lvl).at(marker+1) < min_in_pair)
					min_in_pair = triangle.at(lvl).at(marker+1);

				triangle.at(lvl-1).at(marker) += min_in_pair;
			}
		}

		return triangle.at(0).at(0);
	}
};
