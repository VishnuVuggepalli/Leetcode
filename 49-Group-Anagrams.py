class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedRes = {}
        for i in range(len(strs)):
            a = ''.join(sorted(strs[i]))
            if a not in groupedRes:
                groupedRes[a] = [strs[i]]
            else:
                groupedRes[a] += [strs[i]]
        return list(groupedRes.values())