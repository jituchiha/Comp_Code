# Contains Duplicate

# Brute force 
# Check for each and every pair and find if there's any duplicates present in the array.
# Time Complexity : O(n^2)
# Space Complexity: O(1)
# Verdict: TLE

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        
        return False

# Optimized 
# Sort the array and check for duplicates
# Time Complexity : O(nlogn)
# Space Complexity: O(1)
# Verdict: Accepted



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()

        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                return True

        return False
        





# Best case approach
# Add all elements to a set and then check for the size of original array to that of the set.
# Time Complexity : O(n)
# Space Complexity: O(n)
# Verdict: Accepted




class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        s = set()

        for i in range(len(nums)):
            s.add(nums[i])

        return False if len(s)==len(nums) else True

        