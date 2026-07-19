class Solution:
    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        sub_ans = []

        def dfs(i: int, target: int):
            if target == 0:
                ans.append(sub_ans.copy())
                return
            if target < 0 or i == len(candidates):
                return

            # choose i
            sub_ans.append(candidates[i])
            # i is still reusable
            dfs(i, target - candidates[i])

            # skip i
            sub_ans.pop()
            # i is skipped, only later numbers can be used
            dfs(i + 1, target)

        dfs(0, target)

        return ans

    def combination_sum_dp(self, candidates: list[int], target: int) -> list[list[int]]:
        dp = [[] for _ in range(target + 1)]

        for num in candidates:
            for i in range(num, target + 1):
                if i == num:
                    dp[i].append([num])

                for comb in dp[i - num]:
                    dp[i].append(comb + [num])

        return dp[target]
