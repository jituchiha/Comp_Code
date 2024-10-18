class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute Force
        # I would sort the characters in each string and join it in a string and then check if they are present in the dictionary if not then I would create a new group for storing the sorted strings. Basically storing sorted strings as key and values if they match the sorted string. 
        # TC: O(n*klogk)
        # SC: O(nk)
        # AC
        # anagrams = {}

        # for s in strs:
        #     sorted_string = ''.join(sorted(s))
        #     #print(sorted_string)
        #     if sorted_string not in anagrams:
        #         anagrams[sorted_string] = []
            
        #     anagrams[sorted_string].append(s)
        # #print(anagrams)
        # return list(anagrams.values())

        # Optimized Solution
        # Using count array by storing all of the counts of each string and then checking each string if they have the same character count as anagrams would have same character count.
        # TC: O(n*k)
        # SC: O(nk)
        # AC

        anagrams={}

        for s in strs:
            count = [0] * 26
            
            for char in s:
                count[ord(char) - ord('a')] +=1 

            count_tuple = tuple(count)
            #print(count_tuple)
            if count_tuple not in anagrams:
                anagrams[count_tuple] = []

            anagrams[count_tuple].append(s)


        return list(anagrams.values())