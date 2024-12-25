# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        \\\
        Do not return anything, modify head in-place instead.
        \\\
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second_half = slow.next 
        slow.next = None # remove second half from initial list
        reversed_list = None

        # reverse the second list 
        
        while second_half:
            temp = second_half.next
            second_half.next = reversed_list
            reversed_list = second_half
            second_half = temp
        
        # prev has the reversed list

        first = head
        second = reversed_list

        while second:
            part_2 , part_1 = first.next , second.next

            first.next, second.next = second , part_2
            first , second = part_2, part_1