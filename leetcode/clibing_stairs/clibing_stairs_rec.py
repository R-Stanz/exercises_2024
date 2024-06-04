# Too Complex (Time Limit Exceeded)
class Solution(object):
    def climbStairs(self, n):
	if (n == 1):
		return 1
	elif (n == 2) :
		return 2
	else:
		return self.climbStairs(n-1) + self.climbStairs(n-2)
