#Given a binary tree, you need to compute the length of the diameter of the tree.
#The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
#This path may or may not pass through the root.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        self.dia=1
        def height(root):
            if not root:
                return 0
            hleft=height(root.left)
            hright=height(root.right)
            self.dia = max(self.dia,hleft+hright+1)
            return max(hleft,hright)+1
        height(root)
        return self.dia-1
