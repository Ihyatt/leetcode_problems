# Validate Binary Search Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        result = []
        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            result.append(node.val)
            inorder_traversal(node.right)
        
        inorder_traversal(root)
        threshold = result[0]
        for i, value in enumerate(result[1:]):
            if value <= threshold:
                return False
            threshold = max(value, threshold)
        return True
            