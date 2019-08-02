# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1num = 0
        i = 1
        while l1:
            l1num = l1num + l1.val*i
            i*=10
            l1 = l1.next
        l2num = 0
        j = 1
        while l2:
            l2num = l2num + l2.val*j
            j*=10
            l2 = l2.next
        answer = l1num+l2num
        root = n = ListNode(0)
        if answer == 0:
            n.next = ListNode(0)
            return root.next
        while answer >= 1:
            n.next = ListNode(answer%10)
            answer //= 10
            n = n.next
        return root.next
