# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.l = ListNode()
        self.last = self.l
        lists = [x for x in lists if x != None]
        # While lists is not empty
        while lists != []:
        # Find the smallest head in lists
            smallest_head = min(lists, key=lambda head: head.val)
            smallest_index = lists.index(smallest_head)
        # Remove it from lists and push it onto the new list
            moving_node = lists[smallest_index]
            lists[smallest_index] = lists[smallest_index].next
            self.push(moving_node)
        # If the list it was removed from is now empty, remove it from the list
            if lists[smallest_index] == None:
                del lists[smallest_index]
        # Remove the head node of the new list and return. 
        return self.l.next

    def push(self, new_node) -> None:
        self.last.next = new_node
        self.last = self.last.next
        self.last.next = None
        
