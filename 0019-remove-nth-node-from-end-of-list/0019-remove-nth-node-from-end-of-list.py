class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        curr = head
        cnt = 0

        while curr:
            cnt += 1
            curr = curr.next

        c = cnt - n

        prev = dummy
        temp = head

        while c:
            prev = temp
            temp = temp.next
            c -= 1

        prev.next = temp.next

        return dummy.next