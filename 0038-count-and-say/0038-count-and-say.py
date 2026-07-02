class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
    
        result = "1"

        for _ in range(n - 1):

            curr = []
            count = 1

            for i in range(1, len(result)):

                if result[i] == result[i - 1]:
                    count += 1
                else:
                    curr.append(str(count))
                    curr.append(result[i - 1])
                    count = 1

            curr.append(str(count))
            curr.append(result[-1])

            result = "".join(curr)

        return result