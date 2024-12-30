# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry =0
        dummy = ListNode(0)
        added_numbers = dummy 

        while l1 or l2 or carry:
            dig_sum = carry

            if l1:
                dig_sum += l1.val
                l1 = l1.next
            if l2:
                dig_sum += l2.val
                l2 =  l2.next
            
            carry = dig_sum // 10
            added_numbers.next = ListNode(dig_sum % 10)
            added_numbers = added_numbers.next
        return dummy.next
