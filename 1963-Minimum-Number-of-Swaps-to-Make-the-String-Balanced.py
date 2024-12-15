class Solution:
    def minSwaps(self, s: str) -> int:
        '''
        1. [][]
        2. can be [balanced]
        '''
        stack_size = 0
        for bracket in s:
            if bracket == "[":
                stack_size += 1
            else:
                if stack_size > 0:
                    stack_size -= 1 
        return (stack_size+1) //2

        # stack = []
        # for bracket in s:
        #     if stack and (bracket == "]" and stack[-1] == "["):
        #         stack.pop()
        #     else:
        #         stack.append(bracket)
        #     print("Stack: ", stack)
        # if not stack:
        #     return 0
        # elif len(stack) > 2:
        #     return (len(stack)//2) -1
        # else:
        #     return len(stack)-1        