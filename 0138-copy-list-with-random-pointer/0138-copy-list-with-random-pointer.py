class Solution(object):
    def copyRandomList(self, head):

        if head is None:
            return None

        
        temp = head

        while temp:
            nxt = temp.next

            copy = Node(temp.val)
            temp.next = copy
            copy.next = nxt

            temp = nxt

        temp = head

        while temp:
            copy = temp.next

            if temp.random:
                copy.random = temp.random.next

            temp = copy.next

        temp = head

        dummy = Node(-1)
        copy_curr = dummy

        while temp:

            copy = temp.next

            temp.next = copy.next

            copy_curr.next = copy
            copy_curr = copy

            temp = temp.next

        return dummy.next