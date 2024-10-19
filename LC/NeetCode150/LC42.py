class Solution:
    def trap(self, height: List[int]) -> int:
        # Brute Force 
        # For each bar calculate the water trapped and then finally return the sum of all of the water trapped
        # n^2
        # 1
        # tle

        # n = len(height)
        # total_water = 0 

        # for i in range(1,n-1):
        #     left_max = max(height[:i])
        #     right_max = max(height[i+1:])

        #     trapped_water = min(left_max,right_max) - height[i]


        #     if trapped_water > 0:
        #         total_water+=trapped_water


        # return total_water

        # optimized
        # precompute left and right maximum height values, this way it's not space efficient but we can reduce the time complexity
        # n
        # n

        # if not height:
        #     return 0

        # n = len(height)

        # left_max = [0] * n
        # right_max = [0] * n
        # total_water = 0 


        # left_max[0] = height[0]

        # for i in range(1,n):
        #     left_max[i] = max(left_max[i-1],height[i])


        # right_max[n-1] = height[n-1]

        # for j in range(n-2,-1,-1):
        #     right_max[j] = max(right_max[j+1],height[j]) 


        # for i in range(1,n-1):
        #     total_water += min(left_max[i],right_max[i]) - height[i]

        # return total_water


        # Most optimized
        # There's a way to not even use the extra space that we are using now and that is using two pointer approach 
        # n 
        # 1
        # ac

        if not height:
            return 0

        l,r = 0, len(height) -1 

        leftMax, rightMax = height[l], height[r]

        total_water = 0 

        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax=max(leftMax,height[l])
                total_water += leftMax - height[l]

            else:
                r-=1
                rightMax = max(rightMax, height[r])
                total_water += rightMax - height[r]

        return total_water 





        