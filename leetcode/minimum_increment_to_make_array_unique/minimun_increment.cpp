class Solution {
public:
	int minIncrementForUnique(vector<int>& nums) {
		sort(nums.begin(), nums.end());
		double repeated_count = 0;
		double steps = 0;

		for (int i = 1; i < nums.size(); i++) {
			double diff = nums.at(i) - nums.at(i - 1);

			if (diff == 0) {
				repeated_count += 1;
			}
			else if (diff == 1) {
				steps += repeated_count;
			}
			else if (diff > 1) {
				double interval = diff - 1;
				if (interval > repeated_count) {
					interval = repeated_count;
				}

				steps += (repeated_count - (interval - 1) / 2) * interval;
				repeated_count -= interval;
				steps += repeated_count;
			}
		}

		steps += repeated_count * (repeated_count + 1) / 2;

		return (int) steps;
	}
};
