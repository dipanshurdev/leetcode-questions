# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """


        if not root:
            return []

        s1 = [root]
        s2 = []

        while s1:

            node = s1.pop()
            s2.append(node)

            if node.left:
                s1.append(node.left)

            if node.right:
                s1.append(node.right)

        ans = []

        while s2:
            ans.append(s2.pop().val)

        return ans