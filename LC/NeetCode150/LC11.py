class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute Force
        # Check for all pair and find the max area that's possible.
        # n^2
        # 1
        # tle

        # max_area = 0 
        # n = len(height)

        # for i in range(n):
        #     for j in range(i+1,n):
        #         area = min(height[i],height[j]) * (j-i)
        #         max_area = max(area,max_area)

        # return max_area 

        # Optimized Soln
        # We can use two pointer approach to try to find smaller height and then calculate the max area in the same way we have done above
        # n 
        # 1
        # ac

        l,r = 0, len(height) -1 
        max_area = 0 

        while l<r:
            area = min(height[l],height[r]) * (r-l)
            max_area = max(max_area,area)

            if height[l] < height[r]:
                l+=1

            else:
                r-=1

        return max_area
            
        