#Day 1

# Minimum Time Difference 

# Basically we are converting the given time to minutes and then sorting the given times and then returning the minimum difference
# Key part here is checking for the last and first element as it's a circular 24 hour clock
# Time Complexity : O(nlogn)
# Space Complexity: O(n)
# Verdict: ACC


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        times = [] 

        for time in timePoints:
            h,m = map(int, time.split(":"))
            times.append(h*60 + m) #minutes conversion 

        times.sort()

        res = float('inf')

        for i in range(len(times)-1):
            res = min(res, times[i+1]-times[i])

        res = min(res, 1440 + times[0]-times[-1])

        return res
    

# Can do bucket sort but not for this time