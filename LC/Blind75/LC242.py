# Valid Anagram

# Triple solutions
# Keep two maps for each of the strings and then check for each positions if false return false or atlast 
# return True. As mentioned there are better ways to solve as commented in the code.
# Time Complexity : O(n)
# Space Complexity: O(n)
# Verdict: TLE

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t)

        #return Counter(s) == Counter(t)

        if len(s)!=len(t):
            return False

        countS,countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)

        return True if countS == countT else False
