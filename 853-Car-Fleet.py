class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair= []
        time_stack= []

        for car in range(len(speed)):
            pair.append((position[car], speed[car]))
        pair = sorted(pair)[::-1]

        for p,s in pair:
            time = (target-p)/s
            time_stack.append(time)

            if len(time_stack) >=2 and time_stack[-1] <= time_stack[-2]:
                time_stack.pop()

        return len(time_stack)
