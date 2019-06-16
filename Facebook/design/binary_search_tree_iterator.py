# Binary Search Tree Iterator
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = self.re_pop(root)
    
    def re_pop(self, root):
        if not root:
            return []
        stack = [root]
        current = root
        while current:
            if current.left:
                stack.append(current.left)
            current = current.left
        return stack
    
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.stack:
            top = self.stack.pop()
            if top.right:
                self.stack = self.stack + self.re_pop(top.right)
            return top.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()