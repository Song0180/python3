class Solution:
    # Time: O(?)
    # Space: O(?)
    def product_except_self_own_solution(self, nums: list[int]) -> list[int]:
        nums_num = len(nums)
        prefix = []
        suffix = []

        cur_prefix = 1
        for i in range(nums_num):
            if i == 0:
                prefix.append(cur_prefix)
            if i > 0:
                cur_prefix = cur_prefix * nums[i - 1]
                prefix.append(cur_prefix)

        cur_suffix = 1
        for i in range(nums_num - 1, -1, -1):
            if i == nums_num - 1:
                suffix.insert(0, cur_suffix)
            if i < nums_num - 1:
                cur_suffix = cur_suffix * nums[i + 1]
                suffix.insert(0, cur_suffix)

        for i in range(nums_num):
            prefix[i] = prefix[i] * suffix[i]

        return prefix

    def product_except_self_neetcode_solution(self, nums: list[int]) -> list[int]:
        # Time: O(n)
        # Space: O(1)
        nums_num = len(nums)
        ans = [1] * nums_num

        for i in range(1, nums_num):
            ans[i] = ans[i - 1] * nums[i - 1]

        right = 1
        for i in range(nums_num - 1, -1, -1):
            ans[i] = ans[i] * right
            right = right * nums[i]

        return ans
