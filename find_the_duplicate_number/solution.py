class Solution:
    # Time: O(?)
    # Space: O(?)
    def find_duplicate(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            # number may be marked negative, to calculate idx must use abs
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                # number may be marked negative already
                return abs(nums[i])

            # mark number as visited
            nums[idx] *= -1
