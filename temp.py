class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        i, j = 0, 1

        while j <= len(s):
            cur_str = s[i:j]

            freq = Counter(cur_str)
            hasDup = False
            for count in list(freq.values()):
                if count > 1:
                    hasDup = True
            if hasDup:
                i += 1
            else:
                res = max(res, j - i)
                j += 1

        return res
