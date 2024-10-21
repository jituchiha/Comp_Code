class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Only approach
        # Pretty straight forward, you have left and right pointers each pointing to start and end of the array and then we have a target to reach and keep searching it using the mid pointer and check if we can find the target and if we do we will just return the index or else we would return -1
        # nlogn 
        # 1 
     
            
        
        left, right = 0, len(nums) -1 

        while left<=right:
            mid = (left + right)//2 

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right -=1

            else:
                left +=1

        return -1
        