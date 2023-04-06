# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, node1: Optional[ListNode]) -> Optional[ListNode]:
        if node1 == None or node1.next == None:
            return node1
        node2 = node1.next
        node3 = node1.next.next
        node2.next = node1
        node1.next = self.swapPairs(node3)
        return node2
