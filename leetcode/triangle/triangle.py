class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for lvl in range(len(triangle)):
            for marker in range(len(triangle[lvl-1])):
                triangle[lvl-1][marker] += min(triangle[lvl][marker:marker+2])

        return triangle[0][0]
