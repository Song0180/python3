from typing import Counter


class Solution:
    # Time: O(n) (2n -> n)
    # Space: O(1) (26 eng chars -> 1)
    def check_inclusion(self, s1: str, s2: str) -> bool:
        target_count = Counter(s1)
        l = 0
        cur_count = {}

        for r in range(len(s2)):
            # grow window
            if s2[r] in target_count:
                cur_count[s2[r]] = 1 + cur_count.get(s2[r], 0)

                # shrink the left until count is valid
                while cur_count[s2[r]] > target_count[s2[r]]:
                    left_char = s2[l]
                    cur_count[left_char] -= 1
                    if cur_count[left_char] == 0:
                        del cur_count[left_char]
                    l += 1

            # shrink window from the left.
            else:
                # a new char not in target appeared, skip all previous window
                l = r + 1
                cur_count.clear()

            if cur_count == target_count:
                return True

        return False
