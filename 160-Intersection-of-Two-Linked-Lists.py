# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        spaceA = headA
        spaceB = headB
        while spaceA != spaceB:
            spaceA = headB if spaceA is None else spaceA.next
            spaceB = headA if spaceB is None else spaceB.next
        return spaceA