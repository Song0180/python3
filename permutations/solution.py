class Solution:
    # Time: O(n!): n is the number of elements in the nums list
    # Space: O(n): the maximum depth of the recursion tree is n
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        sub_ans = []

        # Depth-first search to generate all permutations
        # remained is the set of elements that are not yet in the permutation
        # sub_ans is the current permutation being generated
        # time complexity is O(n!)
        # space complexity is O(n)
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
