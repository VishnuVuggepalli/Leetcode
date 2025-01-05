class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N = len(s)
        shift_calc = [0] * (N +1)
        for start, end, direction in shifts:
            shift_calc[start] += 1 if direction == 1 else -1
            shift_calc[end + 1] += -1 if direction == 1 else 1
        
        for i in range(1,N + 1):
            shift_calc[i] += shift_calc[i-1] 
        
        return ''.join(
            chr(ord('a') + (ord(s[i]) - ord('a') + 26 + shift_calc[i]) % 26) for i in range(N)
        )

        # for i in range(len(s)):
        #     if shift_calc[i] > 0:
        #         if ord(s[i]) + shift_calc[i] > ord('z'):
        #             new_s += chr(ord(s[i]) + shift_calc[i] - 26)
        #         else:
        #             new_s += chr(ord(s[i]) + shift_calc[i])
        #     elif shift_calc[i] < 0:
        #         if ord(s[i]) - shift_calc[i] < ord('a'):
        #             new_s += chr(ord(s[i]) + shift_calc[i] + 26)
        #         else:
        #             new_s += chr(ord(s[i]) + shift_calc[i])
        #     else:
        #         new_s += s[i]
        # return new_s