class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack =[]
        #direction : True for Left , False for right 

        for value in range(len(asteroids)):
            while stack and stack[-1]> 0 and asteroids[value] < 0:
                if stack[-1] < -asteroids[value] :
                    stack.pop()
                    continue
                elif stack[-1] == -asteroids[value]:
                    stack.pop()
                break
            else:
                stack.append(asteroids[value])
        return stack