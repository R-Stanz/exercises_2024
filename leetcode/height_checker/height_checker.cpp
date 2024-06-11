class Solution {
public:
	int heightChecker(vector<int>& heights) {
		vector<int> sorted_heights = heights;
		this->quick_sort(heights, 0, heights.size() - 1);
		int count = 0;
		for (int i = 0; i < heights.size(); i++) {
			if (heights.at(i) != sorted_heights.at(i))
				count += 1;
		}
		return count;
	}

	void quick_sort(vector<int>& heights, int head, int tail) {
		if (head < tail) {
			int pivot = this->partition(heights, head, tail);
			this->quick_sort(heights, head, pivot - 1);
			this->quick_sort(heights, pivot + 1, tail);
		}
	}

	int partition(vector<int>& heights, int head, int tail) {
		int pivot = tail;

		for (int i = tail - 1; i >= head; i--) {
			if (heights.at(i) >= heights.at(pivot)) {

				int tmp = heights.at(i);
				for (int u = i; u < pivot; u++) {
					heights.at(u) = heights.at(u+1);
				}

				heights.at(pivot) = tmp;
				pivot -= 1;
			}
		}
		return pivot;
	}
};
