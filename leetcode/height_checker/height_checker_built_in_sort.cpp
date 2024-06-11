class Solution {
public:
	int heightChecker(vector<int>& heights) {
		vector<int> sorted_heights = heights;
		sort(sorted_heights.begin(), sorted_heights.end());
		int count = 0;
		for (int i = 0; i < heights.size(); i++) {
			if (heights.at(i) != sorted_heights.at(i))
				count += 1;
		}
		return count;
	}
};
