# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        

        ans = []
        curr = root

        while curr:

            if curr.left is None:
                ans.append(curr.val)
                curr = curr.right

            else:
                pred = curr.left

                while pred.right and pred.right != curr:
                    pred = pred.right

                if pred.right is None:
                    pred.right = curr
                    curr = curr.left

                else:
                    pred.right = None
                    ans.append(curr.val)
                    curr = curr.right

        return ans
        