class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.MRU = ListNode(0,0)
        self.LRU = ListNode(0,0)
        self.access_map = {}

        # connect MRU and LRU
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
    
    def remove_at_head(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert_at_tail(self, node):
        prev, nxt = self.MRU.prev , self.MRU
        prev.next = nxt.prev = node
        node.prev , node.next = prev, nxt


    def get(self, key: int) -> int:
        if key not in self.access_map:
            return -1 
        self.remove_at_head(self.access_map[key])
        self.insert_at_tail(self.access_map[key])
        return self.access_map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.access_map:
            self.remove_at_head(self.access_map[key])
        self.access_map[key] = ListNode(key,value)
        self.insert_at_tail(self.access_map[key])

        if len(self.access_map) > self.cap:
            lru = self.LRU.next
            self.remove_at_head(lru)
            del self.access_map[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)