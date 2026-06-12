# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):

        def reverseLinkedList(head):
            if head is None or head.next is None:
                return head

            newHead = reverseLinkedList(head.next)

            front = head.next
            front.next = head
            head.next = None

            return newHead

        if head is None or head.next is None:
            return True

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        newHead = reverseLinkedList(slow.next)

        first = head
        second = newHead

        while second is not None:

            if first.val != second.val:
                reverseLinkedList(newHead)
                return False

            first = first.next
            second = second.next

        reverseLinkedList(newHead)

        return True