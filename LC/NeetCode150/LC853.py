class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Optimized
        # Calculate the time for each car to reach the target given their speed, position and destination s= d/t => t = d/s and then store them as a pair and sorted them in reverse order. And if the penultimate element in stack is greater than the top then pop and finally get the length of the stack
        # nlogn
        # n

        pair = [[p,s] for p,s in zip(position,speed)] 

        stack = [] 

        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)

            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
    








        