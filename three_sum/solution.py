class Solution:
    # Time: O(?)
    # Space: O(?)
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]

                if cur_sum < 0:
                    j += 1
                elif cur_sum > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return res
