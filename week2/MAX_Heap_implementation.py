
class MaxHeap(object):
    def __init__(self, items):
        self.queue = [None] + items
        # Build_Max_Heap(A) for i=n/2 down to 1 do Max_Heapify(A,i)
        for i in range(len(self.queue)//2, 0, -1):
            self.max_heapify(i)

    def left(self, i):
        return i*2

    def right(self, i):
        return i*2+1

    def parent(self, i):
        return i//2

    def insert(self, x):
        self.queue.append(x)
        for i in range(len(self.queue)//2, 0, -1):
            self.max_heapify(i)

    def extract_max(self):
        last = len(self.queue) - 1
        if last == 0:
            print("추출할 요소가 없습니다.")
            return -1

        self.queue[1], self.queue[last] = self.queue[last], self.queue[1]
        max_value = self.queue.pop()
        self.max_heapify(1)
        return max_value

    def heapsort(self):
        print(*self.queue[1:])

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        last = len(self.queue)-1
        largest = i

        if (l <= last) and (self.queue[l] > self.queue[i]):
            largest = l
        if (r <= last) and (self.queue[r] > self.queue[largest]):
            largest = r
        if largest != i:
            self.queue[i], self.queue[largest] = self.queue[largest], self.queue[i]
            self.max_heapify(largest)


h = MaxHeap([1, 2, 3, 4, 5, 6])
print(h.extract_max())
h.heapsort()
h.insert(13)
h.insert(7)
h.heapsort()
print(h.extract_max())
h.heapsort()
