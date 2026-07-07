# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        from collections import deque



        if not root:
            return []

        ans = []
        q = deque([root])
        left_to_right = True

        while q:

            level = []

            for _ in range(len(q)):
                node = q.popleft()

                if left_to_right:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(level)
            left_to_right = not left_to_right

        return ans
        