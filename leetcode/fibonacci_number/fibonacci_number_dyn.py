class Solution:
	def fib(self, n: int) -> int:
		if (n == 0):
			return 0
		elif (n == 1):
			return 1
		

		sec_last = 0
		last = 1

		for i in range(2, n):
			tmp = last + sec_last
			sec_last = last
			last = tmp

		return last + last_sec
