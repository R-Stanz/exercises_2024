class Solution {
public:
	vector<int> getRow(int rowIndex) {
		vector<int> last{1};
		vector<int> next = last;

		for (int i = 1; i <= rowIndex; i++) {
			next = {1};
			for (int u = 1; u <= i; u++) {
				if (u <= i/2)
					next.push_back(last.at(u) + last.at(u-1));
				else
					next.push_back(next.at(i - u));
			}
			last = next;
		}
		return next;
	}
};  
