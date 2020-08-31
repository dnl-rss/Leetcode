# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        
        Recursive property: any valid paths containing the root node, 
        must contain all valid paths from the L and R subtrees,
        where the value of the root node is subtracted from the 'sum' parameter
  
        Base case: if the root node is a leave, 
        it is a valid path only if it matches the 'sum' parameter 
        """
        #Edge case: node is null, 
        #           no paths with value sum can exist
        if not root:
            return []

        #Base case: node is a leave, 
        #           if it matches the sum value, return that node as a path
        #           otherwise, return no paths
        if not root.left and not root.right:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        
        #Recursive case: node is not a leave,
        #                any valid paths come from either the L or R subtree
        #                with the node value subtracted from the sum parameter
        paths = self.pathSum(root.left,sum-root.val) + 
                self.pathSum(root.right,sum-root.val)
            
        return [ [root.val]+path for path in paths if path]
