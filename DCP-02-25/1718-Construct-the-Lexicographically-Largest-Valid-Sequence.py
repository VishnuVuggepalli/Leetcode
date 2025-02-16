class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        seqLen = ((n-1) * 2) + 1
        sequence = [0] * seqLen
        visited = set()
        
        def backtrack(index):
            if index == len(sequence): return True

            for num in range(n,0,-1):
                if num in visited:
                    continue
                if num > 1 and (index + num >= seqLen or sequence[index + num]):
                    continue
                
                visited.add(num)
                sequence[index] = num
                if num > 1:
                    sequence[index + num] = num
                
                j = index + 1
                while j < seqLen and sequence[j]:
                    j += 1
                
                if backtrack(j):
                    return True
                
                visited.remove(num)
                sequence[index] = 0
                if num > 1:
                    sequence[index + num] = 0
                
        
        backtrack(0)
        return sequence