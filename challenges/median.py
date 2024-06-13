from numpy import median, array

def median_by_group(arr):
    group_size = arr.pop(0)
    np_arr = array(arr)

    median_arr = [median(np_arr[:i]) \
                    for i in range(1, group_size, 1)]

    median_arr += [median(np_arr[i:i+group_size]) \
                    for i in range(0, len(arr) + 1 - group_size, 1)]

    return median_arr


arr = [2, 3, 1, 2, 3, 4]
print(median_by_group(arr))
