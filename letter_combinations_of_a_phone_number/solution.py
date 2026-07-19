class Solution:
    # Time: O(n * 4^n)
    # Space: O(n) for auxiliary, O(n * 4^n) for answers
    def letter_combinations(self, digits: str) -> list[str]:
        res = []
        sub = []

        if not digits:
            return res

        def dfs(i):
            if i == len(digits):
                # O(n)
                res.append("".join(sub))
                return

            chars = self.get_chars(digits[i])
            # O(4^n)
            for c in chars:
                sub.append(c)
                dfs(i + 1)
                sub.pop()

        dfs(0)
        return res

    def get_chars(self, digit):
        digit_to_chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if digit not in digit_to_chars:
            return ""

        return digit_to_chars[digit]
