class Solution(object):
    def generate(self, numRows):
        pascal = [[1]]

        for i in range (1, numRows):
                new = []
                last = pascal[-1]

                for u in range (0, i+1):
                        first_half = i // 2
                        if (u == 0):
                                new += [1]
                        elif (u <= first_half):
                                new += [last[u] + last[u-1]]
                        else:
                                new += [new[i - u]]

                pascal += [new]
        return pascal
