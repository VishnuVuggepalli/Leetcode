class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq_digits= []
        for i in range(1,10):
            num = i
            next_dig = i + 1

            while num <= high and next_dig <= 9:
                num = num * 10 + next_dig
                next_dig += 1
                if low <= num <= high:
                    seq_digits.append(num)
        seq_digits.sort()
        return seq_digits