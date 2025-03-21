# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        cur = dummy
        while cur:
            while cur.next and cur.next.val == val:
                if cur.next is not None:
                    cur.next = cur.next.next
            cur = cur.next
        return dummy.next
            