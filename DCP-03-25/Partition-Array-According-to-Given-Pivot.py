class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l =[]
        g =[]
        res= []

        for i in nums:
            if i < pivot:
                l.append(i)
            elif i > pivot:
                g.append(i)
            else:
                res.append(i)
        
        return l + res + g