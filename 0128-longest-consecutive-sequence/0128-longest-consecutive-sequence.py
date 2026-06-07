class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        if n == 0:
            return 0

        longest = 1
        st = set(nums)

        for num in st:

            if num - 1 not in st:

                cnt = 1
                x = num

                while x + 1 in st:
                    x += 1
                    cnt += 1

                longest = max(longest, cnt)

        return longest