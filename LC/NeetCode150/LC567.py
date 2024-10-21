# inc
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute Force
        # kinda obvious generate all permutations and check if permutation of s1 is in s2 
        # n!*m m=> len(s2)
        # n!*n
        # tle
        # perms = set([''.join(p) for p in permutations(s1)])

        # for perm in perms:
        #     if perm in s2:
        #         return True 


        # return False 
        
        # Optimised 
        # Create a frequency count of characters in s1 and then maintain a frequency count of characters in s2. Slide across s2 and compare the freq. count of the window with s1 and check if it's equal
        # n 
        # 1

        if len(s1) > len(s2):
            return False 

        s1_count = [0] * 26 
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] +=1
            s2_count[ord(s2[i]) - ord('a')] +=1

        if s1_count == s2_count:
            return True 

        for i in range(len(s1),len(s2)):
            s2_count[ord(s2[i]) - ord('a')] +=1

            s2_count[ord(s2[i - len(s1)]) - ord('a')] -=1

            if s1_count == s2_count:
                return True 

        return False 


