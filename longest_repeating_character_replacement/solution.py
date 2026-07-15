class Solution:
    # Time: O(n)
    # Space: O(m) ~ O(1) as only 26 uppercase chars
    def character_replacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        max_freq = 0

        # grow the window linearly from the right
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[s[r]])

            # sub_len - max_freq > k means k cannot cover the char replacement, illegal.
            # shrink the window from the left until it’s legal again.
            # we can only shrink from the left to discard some chars until k can cover.
            while r - l + 1 - max_freq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
