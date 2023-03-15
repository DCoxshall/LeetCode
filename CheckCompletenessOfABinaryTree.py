# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        frontier = [root]
        while len(frontier) != 0:
            frontier_len = len(frontier)        
            for _ in range(frontier_len):
                node = frontier.pop(0)
                frontier.extend([node.left, node.right])
            
            if None in frontier: # We've reached the leaf node level

                # Check all remaining nodes are leaf nodes
                for node in frontier:
                    if node != None:
                        if node.left != None or node.right != None:
                            return False
            
                # Check that there are no nodes after the None we just found
                for i in range(len(frontier)):
                    if frontier[i] == None:
                        for j in range(i, len(frontier)):
                            if frontier[j] != None:
                                return False
                        return True
