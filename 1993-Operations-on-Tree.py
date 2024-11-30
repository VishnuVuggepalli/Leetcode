class LockingTree:

    def __init__(self, parent: List[int]):
        self.locks = [0 for _ in range(len(parent))]
        self.parent = parent 
        self.children = collections.defaultdict(list)
        for child, parent in enumerate(parent) : self.children[parent].append(child)

    def lock(self, num: int, user: int) -> bool:
        if self.is_locked(num):return False
        self.locks[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num] != user: return False
        self.locks[num] = 0
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.is_locked(num): return False
        if self.locked_ancestors(num) : return False
        if not self.locked_descendants(num) : return False
        self.lock(num,user)
        stack = [num for num in self.children[num]]
        while stack:
            root = stack.pop()
            self.locks[root] =0
            stack.extend(self.children[root])
        return True
    
    def is_locked(self, num:int) -> bool:
        return self.locks[num] != 0
    
    def locked_descendants(self, num:int) -> bool:
        stack =[num for num in self.children[num]]
        while stack:
            root = stack.pop()
            if self.is_locked(root): return True
            stack.extend(self.children[root])
        return False

    def locked_ancestors(self, num:int):
        while self.parent[num] != -1:
            if self.is_locked(self.parent[num]): return True
            num = self.parent[num]
        return False
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)