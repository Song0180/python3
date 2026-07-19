from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def reorder_list(self, head: ListNode[int] | None) -> None:
        slow = fast = head

        # 1: find mid point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2: reverse second half
        second, cur = None, slow.next
        # don't for get to cut first half
        slow.next = None

        while cur:
            temp = cur.next
            cur.next = second
            second = cur
            cur = temp

        # 3: merge first and second
        first = head

        # second is equal or shorter, we can stop after second list is traversed
        while second:
            tmp1, tmp2 = first.next, second.next
            # alternate
            first.next = second
            second.next = tmp1

            # progress
            first = tmp1
            second = tmp2
