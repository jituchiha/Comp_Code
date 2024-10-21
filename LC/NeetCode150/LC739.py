class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force 
        # Iterate through the array and in other loop traverse the array to find the temperature which is warmer than the current one 
        # n^2 
        # n 
        # tle
        # n = len(temperatures)
        # answer = [0]*n
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if temperatures[j]>temperatures[i]:
        #             answer[i]=(j-i)
        #             break

        # return answer

        # Optimized Approach
        # Monotonic Decreasing stack, basically if we find a value that is less than temp value in stack then we pop and store the difference to the result array 
        # n
        # n 
        # ac 

        n = len(temperatures)
        answer = [0]*n

        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                #print(temperatures[stack[-1]])
                index = stack.pop()
                answer[index] = i - index 

            stack.append(i)

        return answer 
        