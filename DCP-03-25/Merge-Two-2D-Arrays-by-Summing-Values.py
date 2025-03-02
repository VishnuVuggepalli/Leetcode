class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0

        N , M = len(nums1), len(nums2)
        res = []

        while i < N and j < M:
            if nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        
        while i < N:
            res.append(nums1[i])
            i += 1
        
        while j < M :
            res.append(nums2[j])
            j += 1
        
        return res