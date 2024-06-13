class Solution {
public:
	void generate_sequences(vector<string>& vec, int max, int count_open = 0, int count_close = 0, string sequence = "") {
		if (max > count_open) {
			generate_sequences(vec, max,count_open + 1, count_close, sequence + "(");
		}
		if (count_close < count_open) {
			generate_sequences(vec, max, count_open, count_close + 1, sequence + ")");
		}
		if (count_close == max) {
			vec.push_back(sequence);
		}
	}

	vector<string> generateParenthesis(int n) {
		vector<string> vec;
		this->generate_sequences(vec, n);
		return vec;
	}
};
