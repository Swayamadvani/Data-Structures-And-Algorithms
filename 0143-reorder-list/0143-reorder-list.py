class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 1. Find middle
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split
        first = head
        second = slow.next
        slow.next = None

        # 3. Reverse second half
        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev

        # 4. Merge
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2