class Solution {
public:
    int climbStairs(int n) {
	if (n == 1)
		return 1;
	else if (n == 2)
		return 2;


	int last = 2;
	int sec_last = 1;

	for (int i = 2; i < n; i++) {
		int tmp = last + sec_last;
		sec_last = last;
		last = tmp;
	}

	return last;
    }
};
