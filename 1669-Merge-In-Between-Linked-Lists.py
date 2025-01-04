# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count = 0
        dummy = ListNode(0,list1)
        prev = dummy

        while prev:
            if count == a:
                temp = prev.next
                prev.next = list2
                while prev.next:
                    prev = prev.next
                while count <= b:
                    count += 1
                    temp = temp.next
                prev.next = temp
            else:
                count += 1
                prev = prev.next
        return dummy.next