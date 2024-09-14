#Day 2
# LONGEST SUBARRAY WITH MAXIMUM BITWISE AND


# Singleton Solution
# On observation and based on the property of bitwise AND max sum would be generated only if we take the same number or else it would 
# be less or even zero in most subarrays so check for streaks based on that logic
# Time Complexity : O(n)
# Space Complexity: O(1)
# Verdict: ACC



class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        ans=streak=max_val=0

        for num in nums:
            if max_val<num:
                max_val = num
                ans=streak = 0

            if max_val == num:
                streak+=1
            else:
                streak=0


            ans = max(ans,streak)

        return ans
        