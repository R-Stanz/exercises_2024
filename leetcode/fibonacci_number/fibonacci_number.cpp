class Solution {
public:
	int fib(int n) {
		if (n <= 1)
			return n;
		
		int sec_last = 0;
		int last = 1;

		for (int i = 2; i <= n; i++) {
			int tmp = last + sec_last;
			sec_last = last;
			last = tmp;
		}
		return last;
	}
};
