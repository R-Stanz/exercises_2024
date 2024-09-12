from queue import Queue

class MinHeap:
    def __init__(self):
        self.heap = [0]

    def size(self):
        return len(self.heap) - 1

    def top(self):
        return self.heap[1]

    def pop(self, index = 1):
        min_value = self.heap[index]
        self.heap[index] = self.heap.pop()
        self.move_down(index)
        return min_value

    def add(self, value):
        self.heap.append(value)
        self.move_up(self.size())

    def update_value(self, old_value, new_value):
        index = self.index(old_value)
        if index > 0:
            self.heap[index] = new_value
            if new_value < old_value:
                self.move_up(index)
            else:
                self.move_down(index)

    def index(self, value):
        to_visit = Queue()
        visiting = 1
        while visiting <= self.size():
            if self.heap[visiting] == value:
                return visiting

            elif self.heap[visiting] < value:
                to_visit.put(visiting*2)
                to_visit.put(visiting*2+1)

            if to_visit.empty():
                break
            visiting = to_visit.get()

        print("Value ({}) Not Found On The Heap.".format(value))
        return 0

    def move_up(self, index):
        previous_index = index // 2
        while index > 1 and self.heap[index] < self.heap[previous_index]:
            self.swap(index, previous_index)
            index = previous_index
            previous_index //= 2

    def move_down(self, index):
        next_index = index * 2
        while next_index < self.size() and self.heap[index] > self.heap[next_index]:
            self.swap(index, next_index)
            index = next_index
            next_index *= 2

    def get_next_index(self, index):
        index *= 2
        if index < self.size():
            if self.heap[index] >= self.heap[index+1]:
                return index
            return index+1

        elif index == self.size():
            return index

        return 0


    def swap(self, index_a, index_b):
        self.heap[0] = self.heap[index_a]
        self.heap[index_a] = self.heap[index_b]
        self.heap[index_b] = self.heap[0]

    def __repr__(self):
        return str(self.heap[1:])
