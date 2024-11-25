def get_ceil(arr, target_value):
    head = 0
    tail = len(arr) - 1

    marker = tail // 2

    if not arr or arr[-1] < target_value:
        return None

    while (tail > head):
        if arr[marker] == target_value:
            return target_value

        elif arr[marker] < target_value:
            head = marker + 1
        else:
            tail = marker

        marker = (tail+head)//2
    
    return arr[marker]
