# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        cnt = 1
        cur = head

        while cur.next:
            cur = cur.next
            cnt += 1
        
        cur.next = head
        
        new_cnt = cnt - (k % cnt)
        while new_cnt != 0:
            cur = cur.next
            new_cnt -= 1
        head = cur.next
        cur.next = None 

        return head