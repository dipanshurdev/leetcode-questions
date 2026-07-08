class Solution:
    def buildTree(self, preorder, inorder):

        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        pre_idx = [0]

        def build(left, right):

            if left > right:
                return None

            root_val = preorder[pre_idx[0]]
            pre_idx[0] += 1

            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)