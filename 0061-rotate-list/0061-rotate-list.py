# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    

    def findNthNode(self, temp, k):
        count = 1

        while temp is not None:
            if count == k:
                return temp

            count += 1
            temp = temp.next

        return temp

    def rotateRight(self, head, k):

        if head is None or head.next is None or k == 0:
            return head

        tail = head
        length = 1

        while tail.next is not None:
            tail = tail.next
            length += 1

        k = k % length

        if k == 0:
            return head

        tail.next = head

        newLastNode = self.findNthNode(head, length - k)

        newHead = newLastNode.next

        newLastNode.next = None

        return newHead