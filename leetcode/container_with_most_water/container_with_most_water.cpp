class Solution {
public:
	int maxArea(vector<int>& height) {
		int max_area = 0;
		int next_head = 0;
		int last_head = -1;
		while (next_head != last_head) { 
			last_head = next_head;

			for (int tail = last_head + 1; tail < height.size(); tail++) {

				int water_height = height[tail];
				if (height[tail] > height[last_head]) {
					water_height = height[last_head];
					if (last_head == next_head)
						next_head = tail;
				}

				int current_area = water_height*(tail-last_head);
				if (max_area < current_area)
					max_area = current_area;
			}
		}
		return max_area;
	}
};
