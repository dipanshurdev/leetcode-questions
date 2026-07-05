# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """        
        nodes = []

        q = deque([(root, 0, 0)])  # node, row, col

        while q:
            node, row, col = q.popleft()

            nodes.append((col, row, node.val))

            if node.left:
                q.append((node.left, row + 1, col - 1))

            if node.right:
                q.append((node.right, row + 1, col + 1))

        nodes.sort()  # sort by col, then row, then value

        ans = []
        prev_col = float('-inf')

        for col, row, val in nodes:

            if col != prev_col:
                ans.append([])
                prev_col = col

            ans[-1].append(val)

        return ans