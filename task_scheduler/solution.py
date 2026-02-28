from collections import Counter, deque
import heapq


class Solution:
    # Time: O(?)
    # Space: O(?)
    def least_interval(self, tasks: list[str], n: int) -> int:
        cycle = 0
        freq = Counter(tasks)

        heap = [-f for f in freq.values()]
        heapq.heapify(heap)
        q = deque()

        while heap or q:
            cycle += 1

            if heap:
                # remember, f is negative
                f = heapq.heappop(heap)

                # f + 1 means decrement current frequency
                if f + 1 != 0:
                    q.append((f + 1, cycle + n))

            # task become available at current cycle, add to heap
            if q and q[0][1] == cycle:
                heapq.heappush(heap, q.popleft()[0])

        return cycle
