class Solution:
    def sortColors(self, nums):
        self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort(self, arr, head, tail):
        if ((head < tail) and (head >= 0)):
            left_pivot, right_pivot = self.partition(arr, head, tail)
            self.quick_sort(arr, head, left_pivot - 1)
            self.quick_sort(arr, left_pivot + 1, right_pivot - 1)
            self.quick_sort(arr, right_pivot + 1, tail)

    def partition(self, arr, head, tail):
        left_pivot = head
        right_pivot = tail

        if (arr[left_pivot] > arr[right_pivot]):
            self.swap(arr, left_pivot, right_pivot)

        for i in range(tail - 1, head + 1, -1):
            if ((arr[right_pivot] <= arr[i]) and (i != right_pivot)):
                right_pivot = self.right_shift(arr, i, right_pivot)
            elif ((arr[left_pivot] >= arr[i]) and (i != left_pivot)):
                left_shift = self.left_shift(arr, i, left_pivot)

        return (right_pivot, left_pivot)


    def swap(self, arr, index_a, index_b):
        arr[index_a], arr[index_b] = arr[index_b], arr[index_a]

    def right_shift(self, arr, start, pivot):
        tmp = arr[start]

        for i in range(start, pivot):
            arr[i] = arr[i+1]
        arr[pivot] = tmp

        return pivot - 1

    def left_shift(self, arr, end, pivot):
        tmp = arr[end]

        for i in range(end, pivot, -1):
            arr[i] = arr[i-1]
        arr[pivot] = tmp

        return pivot + 1
