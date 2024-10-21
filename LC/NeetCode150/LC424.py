class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute Force
        # Go through all of the substrings and start counting the frequency from i to j and then calculate the number of replacements we need to make and if the replacements are less than k we are going to return the max length that's possible
        # n^2
        # tle

        # n = len(s)
        # max_length = 0 

        # for i in range(n):
        #     freq = [0] * 26

        #     for j in range(i,n):
        #         freq[ord(s[i]) - ord('A')] +=1

        #         max_freq = max(freq)

        #         if ( j - i + 1 ) - max_freq <=k:
        #             max_length = max(max_length, j-i+1)


        # return max_length


        # optimized
        # We use two pointers left and right to define the sliding window and then we would store the frequency of each character in the window using a hash map and then keep expanding the right and if the number of changes exceeds k then we increment left to shrink the window and also meanwhile keep track of the maximum window size that requires at most k changes. 
        # n 
        # 1
        # ac

        freq = [0] * 26

        left = 0 

        max_length = 0 

        max_freq = 0 

        for right in range(len(s)):
            freq[ord(s[right]) - ord('A')] +=1

            max_freq = max(max_freq, freq[ord(s[right]) - ord('A')])


            while (right - left + 1) - max_freq > k:
                freq[ord(s[left]) - ord('A')] -=1
                left +=1

            max_length = max(max_length, right - left + 1)

        return max_length 
