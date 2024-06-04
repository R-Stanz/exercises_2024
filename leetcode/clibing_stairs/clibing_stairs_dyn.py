class Solution(object):
    def climbStairs(self, n, last = 2, sec_last = 1):
	if (n == 1):
		return 1
	elif (n == 2) :
		return 2

	sec_last = 1
	last = 2
	for i in range (3, n):
		tmp = sec_last + last
		sec_last = last
		last = tmp
	return last
