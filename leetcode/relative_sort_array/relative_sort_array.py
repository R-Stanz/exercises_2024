class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = [i for i in arr1 if (i not in arr2)]
        result = sorted(result)

        for i in arr2[::-1]:
            result = [i for u in range(arr1.count(i))] + result

        return result
