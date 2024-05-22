class Solution {
public:
	int maxArea(vector<int>& height) {
		int max_area = 0;
		int head = 0;
		int tail = height.size() - 1;
		while (head < tail) {

			cout << head << " " << tail;
			int min_height = height[head];
			if (min_height > height[tail])
				min_height = height[tail];

			int current_area = min_height * (tail - head);

			if (min_height == height[head])
				head += 1;
			else
				tail -= 1;

			if (current_area > max_area)
				max_area = current_area;
		}

		return max_area;
	}
};
