# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for l in lists:
            while l is not None:
                min_heap.append(l.val)
                l = l.next
        heapq.heapify(min_heap)

        dummy = ListNode()
        head = dummy
        while min_heap:
            cur_node = heapq.heappop(min_heap)
            head.next = ListNode(cur_node)
            head = head.next
        
        return dummy.next

