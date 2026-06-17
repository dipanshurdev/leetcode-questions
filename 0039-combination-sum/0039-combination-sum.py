class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        

        res = []
        path = []

        def dfs(index, target):

            if target == 0:
                res.append(path[:])
                return

            if index == len(candidates):
                return

            if candidates[index] <= target:
                path.append(candidates[index])
                dfs(index, target - candidates[index])
                path.pop()

            dfs(index + 1, target)

        dfs(0, target)
        return res