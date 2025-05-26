# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr = head
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next
        target = length - n
        if target == 0:
            return head.next
        curr = head
        for _ in range(target - 1):
            curr = curr.next
        curr.next = curr.next.next
        return head

################### USING TWO POINTER ##################
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        left = head
        right = head
        i = 0
        while i < n:
            right = right.next
            i+=1
        if right == None:
            return head.next
        while right.next != None:
            right = right.next
            left = left.next
        left.next = left.next.next
        return head
