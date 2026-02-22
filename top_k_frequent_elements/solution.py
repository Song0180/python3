from collections import Counter
import heapq


class SolutionSort:
    # Time: O(nlogn) worst
    # Space: O(n)
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)

        sorted_keys = sorted(freq.keys(), key=lambda i: freq[i], reverse=True)
        return sorted_keys[:k]


# heap
class SolutionHeap:
    # Time: O(n + klogn) worst
    # Space: O(m + k)
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)

        heap_base = [(-count, num) for num, count in list(freq.items())]

        """
        Python compares tuples lexicographically:

        Compare the first element of each tuple.
        If those are equal, compare the second element, and so on.
        """
        heapq.heapify(heap_base)

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap_base)[1])

        return ans


class SolutionHeap2:
    # Time: O(n + (m+k)logm ) worst nlogn
    # Space: O(m + k)
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        # O(n)
        freq = Counter(nums)

        heap_base = []

        # m * logm
        for num in freq.keys():
            heapq.heappush(heap_base, (-freq[num], num))

        ans = []
        # k * logm
        for _ in range(k):
            ans.append(heapq.heappop(heap_base)[1])

        return ans


class Solution:
    # Time:
    # Space:
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)

        # Count: 0(not used) 1 2 3 4 5 6 (add 1 for the max count case)
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            bucket[count].append(num)

        ans = []

        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
