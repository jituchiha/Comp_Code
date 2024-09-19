# Search in Rotated Sorted Array
# Key part is to figure out the boundary of the binary search. Nested binary search 
# Time Complexity => O(logn)
# Space Complexity => O(1)



class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
                if target<nums[right] and target > nums[mid]:
                    left = mid+1

                else: 
                    right = mid - 1

        return -1

            

            

                

        