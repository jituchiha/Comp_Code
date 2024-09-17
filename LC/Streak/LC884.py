# Day 2
#Uncommon Words from Two Sentences
# Optimized Solution
# Split the sentence into words and then put it in dictionary with the respective counts of words and then check if the dictionary 
# has any key with count of 1 which you can add to list and then finally return
# Time Complexity : O(m+n)
# Space Complexity: O(m+n)
# Verdict: ACC

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        hm,ans = {},[]

        for word in s1.split():
            hm[word] = hm.get(word,0)+1

        for word in s2.split():
            hm[word] = hm.get(word,0)+1

        for word in hm:
            if hm[word] == 1:
                ans.append(word)
        
        return ans
        