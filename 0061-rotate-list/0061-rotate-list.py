# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        cur = head
        n = 1

        while cur.next:
            cur = cur.next
            n += 1

        cur.next = head
        k = k % n

        steps = n - k
        cur = head

        for i in range(steps - 1):
            cur = cur.next

        newHead = cur.next
        cur.next = None

        return newHead
