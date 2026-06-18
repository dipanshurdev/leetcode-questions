class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial

        nums = [str(i) for i in range(1, n + 1)]
        k -= 1  # Convert to 0-based indexing

        ans = []

        while n:
            fact = factorial(n - 1)

            index = k // fact
            ans.append(nums.pop(index))

            k %= fact
            n -= 1

        return "".join(ans)