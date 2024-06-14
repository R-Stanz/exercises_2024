class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums = sorted(nums)
        repeated_count = 0
        steps = 0

        for i in range(1, len(nums)):

            diff = nums[i] - nums[i-1]

            if (diff == 0):
                repeated_count += 1
            elif (diff == 1):
                steps += repeated_count 
            elif (diff > 1):
                interval = diff - 1
                if (interval > repeated_count):
                    interval = repeated_count
                steps += (repeated_count - (interval - 1) / 2) * interval
                repeated_count -= interval
                steps += repeated_count 

        steps += repeated_count * (repeated_count + 1) / 2

        return int(steps)
