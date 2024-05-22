class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        head = 0
        tail = len(height) - 1

        while (head < tail):
            min_height = height[head]
            if (min_height > height[tail]):
                min_height = height[tail]

            tmp_area = min_height * (tail - head)

            if (min_height == height[head]):
                head += 1
            else:
                tail -= 1

            if (max_area < tmp_area):
                max_area = tmp_area

        return max_area
