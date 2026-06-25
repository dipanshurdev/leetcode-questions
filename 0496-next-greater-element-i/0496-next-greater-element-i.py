class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        

        

        stack = []
        nge = {}

        for num in nums2:

            while stack and stack[-1] < num:
                nge[stack.pop()] = num

            stack.append(num)

        while stack:
            nge[stack.pop()] = -1

        ans = []

        for num in nums1:
            ans.append(nge[num])

        return ans