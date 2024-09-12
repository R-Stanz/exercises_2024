from min_heap import MinHeap

heap = MinHeap()
heap.add(2)
heap.add(4)
heap.add(9)
heap.add(1)
heap.add(11)
heap.add(8)

print(heap)
#print(heap.pop(3))
heap.update_value(11, 0.3)
print(heap)
