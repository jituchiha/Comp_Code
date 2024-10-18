class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute Force
        # Sort both of the strings and check if they are equal or not
        # TC: O(N)
        # SC: O(N)
        # AC 
        #return sorted(s) == sorted(t)

        # Most optimized
        # Frequency count or hashmap add count for the elements in s and subtract for the elements in t and then check for zero count and then return true or false based on that.
        # TC: O(N)
        # SC: O(1)
        # AC

        if len(s)!= len(t):
            return False

        count = [0]* 26

        for i in range(len(s)):
            count[ord(s[i])-ord('a')] +=1
            count[ord(t[i])-ord('a')] -=1

        for c in count:
            if c!=0:
                return False


        return True
        