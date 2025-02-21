class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        storage = {}
        stack = []

        for i in reversed(nums2):
            while stack:
                if i < stack[-1]:
                    storage[i] = stack[-1]
                    stack.append(i)
                    break
                else:
                    storage[i] = -1
                    stack.pop()
            if not stack:
                storage[i] = -1
                stack.append(i)
    
        res = []
        for i in nums1:
            res.append(storage[i])
        
        return res