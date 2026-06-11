# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        

        if headA is None or headB is None:
            return None

        temp1 = headA
        temp2 = headB

        while temp1 != temp2:

            temp1 = temp1.next if temp1 else headB
            temp2 = temp2.next if temp2 else headA

        return temp1