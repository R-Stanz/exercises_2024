class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rest_and_val_index = {}
        
        for i in range(len(nums)):
            val = nums[i] 
            if (val in rest_and_val_index):
                return [i, rest_and_val_index[val]]
            rest_and_val_index[target - val] = i
        
        return []
