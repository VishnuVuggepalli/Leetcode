class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        '''
        1. if number keeps incresing , keep counting  this becomes 
        2.  if numbers keep decreasing - split to 1

        intuition - if any number in order , count it 
        '''

        stack = []
        for i in range(len(arr)):
            if not stack or stack[-1] < arr[i]:
                stack.append(arr[i])
            else:
                max_ele = stack[-1]
                while stack and stack[-1] > arr[i]:
                    stack.pop()
                stack.append(max_ele)
        return len(stack)
        # perms = defaultdict(list)

        # if len(arr) == 1:
        #     return 1

        # i , j = 0,1
        # perms[i] = [arr[i]]
        # while j < len(arr):
        # # for i in range(len(arr)-1,-1,-1):
        #     if arr[j] < arr[j-1]:
        #         perms[i].append(arr[j])
        #         j += 1
        #     else:
        #         i = j
        #         perms[i] = [arr[j]]
        #         j += 1
        # return len(perms)
