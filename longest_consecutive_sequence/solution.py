class Solution:
    # Time: O(n)
    # Space: O(n)
    def longest_consecutive(self, nums: list[int]) -> int:
        # Convert the list to a set to remove duplicates and allow O(1) lookup time
        # space complexity is O(n)
        hash_set = set(nums)
        max_len = 0

        # Iterate through the list and check if the current number is the start of a consecutive sequence
        # if it is, then we can check the next number in the sequence
        # if it is not, then we can skip it
        # time complexity is O(n)
        for num in nums:
            if (num - 1) not in hash_set:
                cur_len = 1
                while num + 1 in hash_set:
                    cur_len += 1
                    num += 1
                max_len = max(max_len, cur_len)

        return max_len
