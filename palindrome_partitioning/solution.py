class Solution:
    # Time: O(n*2^n): n is the length of the string
    # Space: O(n*2^n): the maximum depth of the recursion tree is n and the maximum number of partitions is 2^n
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        sub_ans = []

        def dfs(i):
            # no more chars to partition
            if i == len(s):
                ans.append(sub_ans.copy())
                return

            # make selections in later chars
            for j in range(i, len(s)):
                # skip non-palindromes
                if not self.is_valid(s[i : j + 1]):
                    continue

                sub_ans.append(s[i : j + 1])
                dfs(j + 1)
                sub_ans.pop()

        dfs(0)
        return ans

    def is_valid(self, s: str):
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
