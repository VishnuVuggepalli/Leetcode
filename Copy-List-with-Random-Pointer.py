\\\
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
\\\

class Solution:
    def copyRandomList(self, orgi: 'Optional[Node]') -> 'Optional[Node]':
        '''
        we need key to be the address , value os new ptr 

        '''
        if not orgi:
            return None
        ptr_map = {}
        head = orgi
        while head:
            ptr_map[head] = Node(head.val)
            head = head.next
        
        head = orgi
        while head:
            ptr_map[head].next = ptr_map.get(head.next)
            ptr_map[head].random = ptr_map.get(head.random)
            head = head.next
        
        return ptr_map[orgi]

        # if not orgi:
        #     return None
        # head = orgi
        # while head:
        #     new_node = Node(head.val, head.next)
        #     head.next = new_node
        #     head = new_node.next 
        #     # if head: print(head.next.val)
        #     # if head: print(head.val)
        
        # head = orgi
        # while head:
        #     if head.random:
        #         head.next.random = head.random.next 
        #     head = head.next.next

        # old = orgi
        # modified = orgi.next
        # old_ptr = old
        # mod_ptr = modified

        # while old_ptr:
        #     old_ptr.next = old_ptr.next.next
        #     mod_ptr.next = mod_ptr.next.next if mod_ptr.next else None
        #     old_ptr = old_ptr.next
        #     mod_ptr = mod_ptr.next
        # return modified
