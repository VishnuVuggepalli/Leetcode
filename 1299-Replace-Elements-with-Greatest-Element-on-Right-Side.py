class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ele = -1
        for ele in range(len(arr) -1, -1, -1):
            temp = arr[ele]
            arr[ele] = max_ele
            if temp > max_ele:
                max_ele = temp
        return arr
        