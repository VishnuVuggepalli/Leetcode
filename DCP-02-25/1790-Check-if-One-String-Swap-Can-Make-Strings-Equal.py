class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        return count <= 2
        # unEqual_dict = defaultdict()
        # N = len(s1)
        # countA = 0
        # countB = 0
        # for i in range(N):
        #     if s1[i] == s2[i]:
        #         continue
        #     unEqual_dict[s1[i]] = unEqual_dict.get(s1[i], 0) + 1
        #     unEqual_dict[s2[i]] = unEqual_dict.get(s2[i], 0) - 1
        #     if unEqual_dict[s1[i]] == 0:
        #         del unEqual_dict[s1[i]]
        #         countA += 1
        #     if unEqual_dict[s2[i]] == 0:
        #         del unEqual_dict[s2[i]]
        #         countB += 1
        
        # print(countA, countB, len(unEqual_dict))

        # return countA < 2 and countB <2 and len(unEqual_dict) == 0