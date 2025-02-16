class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(string: str, index : int, target: int) -> bool:
            if index == len(string):
                return target == 0
            cur_num = 0
            for j in range(index, len(string)):
                cur_num = cur_num * 10 + int(string[j])

                if cur_num > target:
                    break
                
                if partition(string, j+1, target-cur_num):
                    return True
            return False

        punish_num = 0
        for i in range(1,n+1):
            if partition(str(i * i), 0 , i):
                punish_num += (i * i)
        
        return punish_num