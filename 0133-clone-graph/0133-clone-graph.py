class Solution:
    def cloneGraph(self, node):

        if not node:
            return None

        mp = {}

        def dfs(curr):

            if curr in mp:
                return mp[curr]

            copy = Node(curr.val)
            mp[curr] = copy

            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)