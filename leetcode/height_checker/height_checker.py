class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        return sum([1 for i in range(len(heights)) if (heights[i] != sorted_heights[i])])
