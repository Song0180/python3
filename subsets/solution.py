class Solution:
    # Time: O(2^n): each element has two choices, to be in the subset or not
    # Space: O(n): the maximum depth of the recursion tree is n
    def subsets_recursive(self, nums: list[int]) -> list[list[int]]:
        ans = []
        subset = []

        # Depth-first search to generate all subsets
        # i is the current index of the element in the nums list
        # subset is the current subset being generated
        # time complexity is O(2^n)
        # space complexity is O(n)
        def dfs(i):
            # If we have reached the end of the nums list, add the current subset to the answer and return
            if i == len(nums):
                ans.append(subset.copy())
                return

            # Add the current element to the subset and recurse
            subset.append(nums[i])
            dfs(i + 1)

            # Remove the current element from the subset and recurse
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return ans

    def subsets_iterative(self, nums: list[int]) -> list[list[int]]:
        # Time: O(n * 2^n): for each element in the nums list, we need to create a new subset
        # Space: O(n * 2^n): the maximum number of subsets is 2^n
        ans = [[]]
        for num in nums:
            ans.extend([subset + [num] for subset in ans])
        return ans
