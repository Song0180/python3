from collections import Counter, deque
import heapq


class Solution:
    # Time: O(?)
    # Space: O(?)
    def least_interval(self, tasks: list[str], n: int) -> int:
        cycles = 0
        freq_map = Counter(tasks)
        # always process available tasks with max frequency, use a max_heap to track the most frequent task for O(1) decision
        max_heap = [-f for f in freq_map.values()]
        heapq.heapify(max_heap)

        # use a queue for cooling down. after processing a task, we put it into a queue to wait for it becomes available again
        # the queue stores (updated_frequency, cycle_when_task_becomes_avail)
        q = deque([])

        # process when have available tasks or tasks cooling down
        while max_heap or q:
            cycles += 1

            # available tasks
            if max_heap:
                freq = -heapq.heappop(max_heap)
                new_freq = freq - 1

                # still not finished yet, put in q to cool down
                if new_freq > 0:
                    q.append((-new_freq, cycles + n))

            # cool-down finished, make the task available again
            if q and q[0][1] == cycles:
                heapq.heappush(max_heap, q.popleft()[0])

        return cycles
