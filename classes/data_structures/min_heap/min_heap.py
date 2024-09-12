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

    def rm_by_index(self, index):
        next_index = self.get_next_value(index)
        if next_value > 0:
            self.heap[index] = self.heap.pop(next_index)
        else:
            self.heap.pop(index)

    def get_next_index(self, index):
        index *= 2
        if index < self.size():
            if self.heap[index] >= self.heap[index+1]:
                return index
            return index+1

        elif index == self.size():
            return index

        return 0

    def update_value(self, old_value, new_value):
        pos = self.heap.index(old_value)
        if pos > 0:
            self.heap[pos] = new_value
            if new_value < old_value:
                self.move_up(pos)
            else:
                self.move_down(pos)

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

    def move_up(self, pos):
        previous_pos = pos // 2
        while pos > 1 and self.heap[pos] < self.heap[previous_pos]:
            self.swap(pos, previous_pos)
            pos = previous_pos
            previous_pos //= 2

    def move_down(self, pos):
        next_pos = pos * 2
        while next_pos < self.size() and self.heap[pos] > self.heap[next_pos]:
            self.swap(pos, next_pos)
            pos = next_pos
            next_pos *= 2

    def swap(self, pos_a, pos_b):
        self.heap[0] = self.heap[pos_a]
        self.heap[pos_a] = self.heap[pos_b]
        self.heap[pos_b] = self.heap[0]

    def __repr__(self):
        return str(self.heap[1:])
