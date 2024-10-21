class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Brute Force
        # Start from left to right and find the max area of rectangle possible, explore all of the areas and then decide which one to take. 
        # n^2
        # 1 
        # tle

        # n = len(heights)
        # max_area = 0

        # for i in range(n):
        #     min_height = heights[i]

        #     for j in range(i,n):
        #         min_height = min(min_height, heights[j])
        #         width = j - i + 1 
        #         max_area = max(max_area, min_height * width)

        # return max_area
        
        # optimized 
        # Use a monotonic stack to keep track of maximum area,we will maintain a stack of increasing bar heights and finally if the stack is not empty we will process the remaining stack 
        # n 
        # n 
        # ac

        n = len(heights)
        max_area = 0 

        stack = [] 

        for i in range(n):

            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()] 
                width = i if not stack else i - stack[-1] -1 

                max_area = max(max_area, h * width)

            stack.append(i)

        while stack:
            h = heights[stack.pop()]
            width = n if not stack else n - stack[-1] -1 
            max_area = max(max_area, h * width) 

        return max_area 