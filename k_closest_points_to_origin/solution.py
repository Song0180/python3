import heapq


class Solution:
    # Time: O(?)
    # Space: O(?)
    def k_closest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_h = []

        for point in points:
            dist = -(point[0] ** 2 + point[1] ** 2)

            heapq.heappush(max_h, (dist, point))
            if len(max_h) > k:
                heapq.heappop(max_h)

        return [p[1] for p in max_h]
