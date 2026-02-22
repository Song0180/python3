from collections import defaultdict


class SolutionSort:
    # Time: O(m * nlogn)
    # Space: O(m * n)
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        ans = {}
        for str in strs:
            key = "".join(sorted(str))
            if key in ans:
                ans[key].append(str)
            else:
                ans[key] = [str]
        return ans.values()


class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord("a")] += 1

            # print(tuple(count))

            ans[tuple(count)].append(s)

        return list(ans.values())
