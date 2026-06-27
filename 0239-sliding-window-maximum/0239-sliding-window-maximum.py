class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        

        dq = deque()
        ans = []

        for i in range(len(nums)):

            # Remove indices outside window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Window formed
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans