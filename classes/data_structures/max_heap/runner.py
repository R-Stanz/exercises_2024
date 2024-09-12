from max_heap import MaxHeap

heap = MaxHeap()
heap.add(2)
heap.add(4)
heap.add(9)
heap.add(1)
heap.add(10)
heap.add(8)

print(heap)
print(heap.pop(3))
#heap.update_value(10, 1)
print(heap)
