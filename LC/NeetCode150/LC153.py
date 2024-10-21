class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Optimized 
        # Given the array is sorted that calls for a binary search and here the key part is to check if the minimum value that we are looking for is in the left part of the array or in the right part of the array. Since the array is rotated if the mid is less than left sorted that means we need to search right and if it's greater that means we need to search towards the left. 
        # logn 
        # 1 
        # ac

        res = nums[0]
        l,r = 0,len(nums) -1 

        while l<=r:
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            m = (l+r)//2
            res = min(res,nums[m])

            if nums[m] >=nums[l]:
                l=m+1
            else:
                r = m-1 

        return res 