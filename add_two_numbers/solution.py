from leetcode_py import ListNode


class SolutionRecursive:
    # Time: O(m + n)
    # Space: O(m + n)
    def add_two_numbers(
        self, l1: ListNode[int] | None, l2: ListNode[int] | None
    ) -> ListNode[int] | None:
        ans = ListNode(0)
        self.helper(ans, l1, l2, 0)
        return ans.next

    def helper(
        self,
        ans: ListNode[int],
        l1: ListNode[int] | None,
        l2: ListNode[int] | None,
        carry: int,
    ) -> None:
        if not l1 and not l2 and carry == 0:
            return

        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        new_carry, new_val = divmod(carry + v1 + v2, 10)
        ans.next = ListNode(new_val)
        self.helper(
            ans.next, l1.next if l1 else None, l2.next if l2 else None, new_carry
        )
        return


class Solution:
    # Time: O(m + n)
    # Space: O(m + n)
    def add_two_numbers(
        self, l1: ListNode[int] | None, l2: ListNode[int] | None
    ) -> ListNode[int] | None:
        ans = ListNode(0)
        cur = ans

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            carry, new_val = divmod(carry + v1 + v2, 10)

            cur.next = ListNode(new_val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return ans.next
