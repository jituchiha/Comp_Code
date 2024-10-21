class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Optimized 
        # We have to use binary search since the matrix is sorted but the key here is to know how to go through the list and search for values, we can do that by mapping the 2d array into 1D indices how? 
        # index = row * n + col  and row = index//n, col = index % n, now that we know this it become again a simple binary search problem 
        # log(m*n)
        # 1 

        if not matrix or not matrix[0]:
            return False 

        m,n = len(matrix) , len(matrix[0])

        left,right = 0, m*n -1 

        while left<=right:
            
            mid = (left + right)//2

            row = mid //n 

            col = mid % n 

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                left +=1 

            else:
                right -=1 

        
        return False 

        