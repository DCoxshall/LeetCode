# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse_linked_list(head):
            x = head
            y = head.next
            head.next = None

            while y != None:
                z = y.next
                y.next = x
                x = y
                y = z
            
            return x

        if left == right:
            return head

        # `top` remains `None` if the reversed segment starts at the head.
        # Otherwise, it contains everything before the reversed segment.
        top = None
        if left > 1:
            top = head

        # `mid` represents the segment of the array we are supposed to reverse.
        mid = head
        for _ in range(1, left):
            mid = mid.next

        # `bot` represents everything after the segment of the array we're
        # supposed to reverse.
        bot = head
        for _ in range(0, right):
            bot = bot.next

        # We need to disconnect `top` from `mid`, and `mid` from `bot`.
        t = top
        if t != None:
            for _ in range(1, left-1):
                t = t.next
            t.next = None
        
        m = mid
        for _ in range(right - left):
            m = m.next
        m.next = None

        # At this point, we have three linked lists: `top`, which is everything
        # before the segment we're supposed to reverse, `mid`, which is the head
        # of the segment we're supposed to reverse, and `bot`, the everything
        # after the segment we're supposed to reverse.
        # We also have `t`, which is the last node of `top` (if `top` exists),
        # and `m`, which is the last node of `mid`.

        # We reverse `mid`, and recalculate `m`.
        mid = reverse_linked_list(mid)

        m = mid
        while m.next != None:
            m = m.next

        # Finally, we reconnect the three lists and return.
        m.next = bot

        if top == None:
            return mid
        else:
            t.next = mid
            return top
