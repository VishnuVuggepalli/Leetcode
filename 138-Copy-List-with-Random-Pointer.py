\\\
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
\\\

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        old_new = {None:None}
        cur = head

        while cur:
            copy = Node(cur.val)
            old_new[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = old_new[cur]
            copy.next = old_new[cur.next]
            copy.random = old_new[cur.random]
            cur = cur.next
        
        return old_new[head]
        # cur = head
        # while cur:
        #     copy = Node(cur.val, cur.next)
        #     cur.next = copy
        #     cur = copy.next
        
        # cur = head
        # while cur:
        #     if cur.random:
        #         cur.next.random = cur.random.next
        #     cur = cur.next.next
        
        # old_head = head
        # new_head = head.next
        # old_cur = old_head
        # new_cur = new_head

        # while old_cur:
        #     old_cur.next = old_cur.next.next
        #     new_cur.next = new_cur.next.next if new_cur.next else None
        #     old_cur = old_cur.next
        #     new_cur = new_cur.next
        
        # return new_head
        