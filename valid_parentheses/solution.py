class Solution:
    # Time: O(n)
    # Space: O(n)
    def is_valid(self, s: str) -> bool:
        stack = []
        hash_map = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in hash_map:
                if not stack or stack[-1] != hash_map[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)

        return not stack
