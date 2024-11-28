class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack= []
        right =0
        for element in range(len(pushed)):
            stack.append(pushed[element])
            # print(stack, stack[-1])
            while stack and stack[-1] == popped[right]:
                stack.pop()
                right+=1        
        if len(stack) > 0:
            return False
        return True