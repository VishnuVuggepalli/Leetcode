class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []
        final =[]
        c = [0]*128
        for i in range(len(p)):
            c[ord(p[i])] += 1

        res = [0]*128

        for right in range(len(p)):
            res[ord(s[right])]+=1
            if c == res:
                final.append(right - (len(p) -1))
        right += 1
        left = 0
        while right< len(s):
            res[ord(s[left])] -=1
            left += 1
            res[ord(s[right])] +=1
            print(left, right)
            if c == res:
                final.append(left)
            right +=1 
        return final
                    