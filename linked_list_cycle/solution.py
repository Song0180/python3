from leetcode_py import ListNode


class Solution:
    # Time: O(?)
    # Space: O(?)
    def has_cycle(self, head: ListNode[int] | None) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # do not use "==" for comparison
            if fast is slow:
                return True

        return False
