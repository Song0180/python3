from leetcode_py import ListNode


class Solution:
    # Time: O(m + n)
    # Space: O(1)
    def merge_two_lists_iterative(
        self, list1: ListNode[int] | None, list2: ListNode[int] | None
    ) -> ListNode[int] | None:
        head = cur = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            cur = cur.next

        cur.next = list1 or list2

        return head.next

    # time: O(m + n)
    # space: O(m + n)
    def merge_two_lists(
        self, list1: ListNode[int] | None, list2: ListNode[int] | None
    ) -> ListNode[int] | None:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.merge_two_lists(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_two_lists(list1, list2.next)
            return list2
