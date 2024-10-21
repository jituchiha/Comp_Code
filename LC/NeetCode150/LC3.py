class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute Force 
        # Iterate through the given string and compute all of the substrings and check for the longest substring and make sure you use set to check if they are repeated or not.
        # n^3
        # n
        # tle

        # n = len(s)
        # max_length = 0 

        # for i in range(n):
        #     for j in range(i+1,n+1):
        #         substring = s[i:j]

        #         if len(substring) == len(set(substring)):
        #             max_length = max(max_length, j-i)

        # return max_length

        # Optimized
        # sliding window with hashset. We will use two pointers left and right. When we find duplicate then we would update the left pointer to the next one and our right pointer will be like an iterator (i) 
        # n 
        # min(n,m) (m=>char_set size)

        # char_set = set()

        # max_length,left = 0,0

        # for right in range(len(s)):

        #     while s[right] in char_set: # duplicate skipping 
        #         char_set.remove(s[left])
        #         left+=1

        #     # update the max length by adding the character to the set 
        #     char_set.add(s[right])
        #     max_length = max(max_length, right - left + 1)

        # return max_length

        # Optimized 
        # Same thing using sliding window but with hashmap, debaitable if this is better solution that set but it's better than brute force
        # n 
        # min(m,n) 
        # ac

        char_map = {}

        left, max_length = 0,0

        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1

            char_map[s[right]] = right

            max_length = max(max_length, right-left + 1) 


        return max_length
        



    

        