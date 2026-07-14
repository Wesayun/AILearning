'''Leetcode#206
I copy the rare answer below
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        pre = None
        while h:
            next = h.next
            h.next = pre
            pre = h
            h = next
        return pre