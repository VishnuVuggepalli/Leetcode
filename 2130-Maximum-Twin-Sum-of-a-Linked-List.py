# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # reverse of first half of list
        # to find half , fast and slow 
        fast = slow = head
        reversed_half = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = reversed_half
            reversed_half = slow
            slow = temp
        
        # Add vals of two lists and validate max sum
        max_twin_sum = 0
        while slow:
            max_twin_sum = max(max_twin_sum , slow.val + reversed_half.val)
            slow = slow.next
            reversed_half = reversed_half.next
        
        return max_twin_sum