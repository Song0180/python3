class Solution:
    # Time: O(?)
    # Space: O(?)
    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        # monotonic decreasing stack, as only same or smaller new values can be inserted
        stack = []

        for i, t in enumerate(temperatures):

            # found a temp higher than prev temps in stack
            while stack and t > stack[-1][0]:
                _, idx = stack.pop()
                res[idx] = i - idx

            # add current temp, idx in stack
            stack.append((t, i))
        return res
