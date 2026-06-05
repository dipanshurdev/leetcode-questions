class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans = float(1.0)
        nn = int(n)

        if(nn<0): nn = -1 * nn;
        while(nn> 0):
            if(nn%2 == 1):
                ans = ans * x;
                nn = nn -1;
            else:
                x = x*x
                nn = nn/2
        
        if(n<0): ans = float(1.0)/float(ans)
        return ans