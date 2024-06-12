class Solution {
public:
	vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
		map<int, int> val_frequency;
		for (int i : arr1) {
			val_frequency[i] += 1;
		}

		vector<int> ans;

		for (int i : arr2) {
			ans.insert(ans.end(), val_frequency[i], i);
			val_frequency.erase(i);
		}

		for (pair<int, int> i : val_frequency) {
			ans.insert(ans.end(), i.second, i.first);
		}

		return ans;
	}
};
