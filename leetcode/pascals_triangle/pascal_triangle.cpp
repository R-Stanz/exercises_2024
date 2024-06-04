class Solution {
public:
	vector<vector<int>> generate(int numRows) {
		vector<vector<int>> pascal(numRows);
		pascal.at(0) = {1};
		
		for (int i = 1; i < numRows; i++) {
			vector<int>& tmp = pascal.at(i);
			vector<int>& old = pascal.at(i-1);

			for (int u = 0; u <= i; u++) {
				if (u == 0)
					tmp.push_back(1);
				else if (u <= i / 2) {
					int tmp_val = old.at(u) + old.at(u-1);
					tmp.push_back(tmp_val);
				}
				else
					tmp.push_back(tmp.at(i - u));
			}
		}
		return pascal;
	}
};
