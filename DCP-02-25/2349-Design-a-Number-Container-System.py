class NumberContainers:

    def __init__(self):
        self.indexes= {}
        self.cur_vals = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.indexes[index] = number
        cur_heap = self.cur_vals[number]
        heapq.heappush(cur_heap, index)


    def find(self, number: int) -> int:
        if number not in self.cur_vals:
            return -1
        # print(self.cur_vals)
        while self.cur_vals[number]:
            smallest = self.cur_vals[number][0]
            if self.indexes.get(smallest) == number:
                return smallest
            
            heapq.heappop(self.cur_vals[number])
        return -1

        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)