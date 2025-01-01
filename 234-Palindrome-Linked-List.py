# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #find mid
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow
        prev = None
        while cur:
            new_node = cur.next
            cur.next = prev
            prev = cur
            cur = new_node
        
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True