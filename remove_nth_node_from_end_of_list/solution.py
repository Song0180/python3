from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def remove_nth_from_end_two_pass(
        self, head: ListNode[int] | None, n: int
    ) -> ListNode[int] | None:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        idx = length - n

        if idx == 0:
            return head.next

        prev = ListNode(0, head)
        cur = head
        step = 0

        while step < idx:
            step += 1
            prev = prev.next
            cur = cur.next

        prev.next = cur.next

        return head

    # time: O(n)
    # space: O(1)
    # single pass, 2 pointers
    def remove_nth_from_end(
        self, head: ListNode[int] | None, n: int
    ) -> ListNode[int] | None:
        dummy = ListNode(0, head)
        first = dummy
        second = head

        for _ in range(n):
            second = second.next

        while second:
            second = second.next
            first = first.next

        first.next = first.next.next

        return dummy.next
