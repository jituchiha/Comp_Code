class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Optimized 
        # Binary search again, we will try to find if the left subarray is sorted or the right one and based on that we update the left and right pointers accordingly. If we finally don't find the right index then we return -1 
        # logn 
        # 1
        n = len(nums)

        left, right = 0, n-1

        while left <= right:
            mid = (left+right)//2
            # Direct find
            if nums[mid] == target:
                return mid
            # left subarray is sorted
            elif nums[mid] >= nums[left]:
                if target >=nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1 
            # right subarray is sorted
            else:
                if target<=nums[right] and target > nums[mid]:
                    left = mid+1

                else: 
                    right = mid - 1

        return -1

            

            

                

        