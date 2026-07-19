import heapq


class MedianFinder:
    # Time: O(1)
    # Space: O(n)
    def __init__(self) -> None:
        self.min_heap = []
        self.max_heap = []

    # Time: O(log(n))
    # Space: O(1)
    def add_num(self, num: int) -> None:
        if self.max_heap and num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # rebalance
        if len(self.max_heap) < len(self.min_heap):
            while len(self.min_heap) - len(self.max_heap) > 1:
                val = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -val)
        else:
            while len(self.max_heap) - len(self.min_heap) > 1:
                val = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -val)

    # Time: O(1)
    # Space: O(1)
    def find_median(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        elif len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]
