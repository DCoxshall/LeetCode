# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = "", ""
        while l1 != None:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2 != None:
            num2 = str(l2.val) + num2
            l2 = l2.next

        num3 = str(int(num1) + int(num2))[::-1]

        ansL = ListNode(num3[0])

        print(num3)

        for i in num3[1:]:
            self.insert(ansL, int(i))

        return ansL


    def insert(self, l: ListNode, v: int):
        if l.next == None:
            l.next = ListNode(v)
        else:
            self.insert(l.next, v)
