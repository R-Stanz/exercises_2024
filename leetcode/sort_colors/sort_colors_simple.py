class Solution:
    def sortColors(self, nums):
        self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort(self, arr, head, tail):
        if (head < tail):
            pivot = self.partition(arr, head, tail)
            self.quick_sort(arr, head, pivot - 1)
            self.quick_sort(arr, pivot + 1, tail)

    def partition(self, arr, head, tail):
        pivot = tail

        for i in range(tail - 1, head - 1, -1):
            if ((arr[pivot] <= arr[i]) and (i != pivot)):
                pivot = self.shift(arr, i, pivot)

        return pivot

    def shift(self, arr, start, pivot):
        tmp = arr[start]

        for i in range(start, pivot):
            arr[i] = arr[i+1]
        arr[pivot] = tmp

        return pivot - 1
