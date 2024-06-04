class Solution:
	def getRow(self, rowIndex: int) -> List[int]:
		if (rowIndex == 0):
			return [1]
		elif (rowIndex == 1):
			return [1,1]

		last = [1,1]

		for i in range(2, rowIndex+1):
			next = [1]
			for u in range(1, i+1):
				if (u <= i//2):
					next += [last[u] + last[u-1]]
				else:
					next += [next[i - u]]
			last = next
		
		return next
