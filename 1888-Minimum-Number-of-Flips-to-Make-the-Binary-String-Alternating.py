class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        odd , eve = defaultdict(int), defaultdict(int)

        for i in range(n):
            if i % 2 == 0:
                eve[s[i]] += 1
            else:
                odd[s[i]] += 1
        
        min_val = min(odd["1"] + eve ["0"] , odd["0"] + eve["1"])

        if n%2 ==0: return min_val

        for i in range(n):
            eve[s[i]] -=1
            odd[s[i]] +=1

            eve , odd = odd, eve

            min_val = min(min_val, odd["1"] + eve ["0"] , odd["0"] + eve["1"])
        return min_val
        # left = 0
        # right = len(s) -1
        # count =0
        # for itr in range(1,len(s)):
        #     if s[itr] == s[itr-1]: 
        #         if s[itr] == s[itr+1]:
        #             if s[itr] == '0':
        #                 s = s[:itr] + '1' + s[itr+1:]
        #             else:
        #                 s = s[:itr] + '0' + s[itr+1:]
        #             count += 1
        #         else:
        #         # if s[left] != s[right]:
        #         #     s = s[left+1 : right+1] + s[left]
        #         # else:
                    
        # print(s)
        # return count