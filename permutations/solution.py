class Solution:
    # Time: O(n!*n^2): n is the number of elements in the nums list
    # Space: O(n*n!): the maximum depth of the recursion tree is n and the maximum number of permutations is n!
    def permute_recursive(self, nums: list[int]) -> list[list[int]]:
        ans = []
        sub_ans = []

        # Depth-first search to generate all permutations
        # remained is the set of elements that are not yet in the permutation
        # sub_ans is the current permutation being generated
        # time complexity is O(n!*n^2)
        def dfs(remained):
            if len(remained) == 0:
                ans.append(sub_ans.copy())
                return

            for num in remained:
                sub_ans.append(num)
                # Create a new set of elements that are not yet in the permutation
                new_remained = remained.copy()
                new_remained.remove(num)
                # Recurse with the new set of elements
                dfs(new_remained)
                # Remove the current element from the permutation
                sub_ans.pop()

        dfs(set(nums))

        return ans


# Time: O(n!*n): n is the number of elements in the nums list
# Space: O(n*n!): the maximum depth of the recursion tree is n and the maximum number of permutations is n!
def permute_optimal(self, nums: list[int]) -> list[list[int]]:
    ans = []
    sub_ans = []

    # Used array to track which elements have been used in the permutation
    used = [False] * len(nums)

    def dfs():
        if len(sub_ans) == len(nums):
            ans.append(sub_ans.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            sub_ans.append(nums[i])
            # Recurse with the next element
            dfs()
            # Remove the current element from the permutation
            sub_ans.pop()
            used[i] = False

    dfs()
    return ans
