class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        

        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for curr_amount in range(1, amount + 1):

            for coin in coins:

                if coin <= curr_amount:
                    dp[curr_amount] = min(
                        dp[curr_amount],
                        1 + dp[curr_amount - coin]
                    )

        return dp[amount] if dp[amount] != float('inf') else -1