from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def reverse_list_iterative(
        self, head: ListNode[int] | None
    ) -> ListNode[int] | None:
        # prev points to the already reversed part of the list.
        # cur points to the node currently being processed.
        prev, cur = None, head

        while cur:
            # save the next node
            temp = cur.next
            # reverse current link
            cur.next = prev
            # update prev to point to the reversed part
            prev = cur
            # move cur forward
            cur = temp

        return prev

    # Time: O(n)
    # Space: O(n)
    def reverse_list(self, head: ListNode[int] | None) -> ListNode[int] | None:
        if not head:
            return None

        new_head = head
        if head.next:
            # Reverse the rest of the list.
            new_head = self.reverse_list(head.next)
            # Make the next node point back to the current node.
            head.next.next = head
        # removes the old forward arrow, break the cycle
        head.next = None

        return new_head
