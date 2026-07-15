class Solution:
    # Time: O(n)
    # Space: O(n)
    def trap_prefix_suffix_arr(self, height: list[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        # first pass, fill left max. at i, the value is max height on the left (including i itself)
        left_max[0] = height[0]
        for i in range(1, n):
            # why compare with i - 1? left_max[i - 1] represents the max height seen at the left already
            left_max[i] = max(left_max[i - 1], height[i])

        # second pass, fill right max.
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        res = 0

        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]

        return res

    # 2 pointers
    # Time: O(n)
    # Space: O(1)
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        res = 0
        while l < r:
            # bounded by left side, so compare left side with current position
            if left_max < right_max:
                l += 1
                # update left max
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                # update right max
                right_max = max(right_max, height[r])
                res += right_max - height[r]

        return res
