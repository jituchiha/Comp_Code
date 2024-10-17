class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

# Brute force
# Traverse every element and check if there's another element like it in the given array
# TC: O(N^2)
# SC: O(1)
# TLE
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True

        # return False


# Optimized 
# Sort and check consecutive elements in the array for duplicates.
# TC: O(NlogN)
# SC: O(1)
# Accepted

        # nums.sort()

        # for i in range(1,len(nums)):
        #     if nums[i-1] == nums[i]:
        #         return True
            
        # return False

# Most optmized
# Store the elements in set as you traverse across the array and check if the set has those elements
# TC: O(N)
# SC: O(N)
# AC
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
