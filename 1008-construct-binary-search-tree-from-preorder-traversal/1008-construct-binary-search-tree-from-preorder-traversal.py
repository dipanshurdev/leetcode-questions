class Solution:

    def bstFromPreorder(self, preorder):

        self.idx = 0

        def build(low, high):

            if self.idx >= len(preorder):
                return None

            val = preorder[self.idx]

            if val <= low or val >= high:
                return None

            self.idx += 1

            root = TreeNode(val)

            root.left = build(low, val)
            root.right = build(val, high)

            return root

        return build(float('-inf'), float('inf'))