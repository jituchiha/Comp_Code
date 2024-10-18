class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute force
        # Sort and then check if the next number is in sequence and if it is update it counter and find the max length out of it
        # nlogn
        # 1 
        # if nums == []:
        #     return 0
        # longest,length = 1,1 

        # nums.sort()
        # i = 0
        # for i in range(len(nums)-1):
        #     if nums[i+1] == nums[i] + 1:
        #         length +=1
        #     elif nums[i+1] == nums[i]:
        #         continue
        #     else:
        #         length = 1
        #     longest = max(longest,length)
            

        # return longest

        # Better approach is to use set and the key logic here is to check if there's something to the left of the sequence if there is then that means it's not the start of the sequence so go until there's no the correct number over there and we use the same logic for checking the end of the sequence if there's something that is at the end or not. 
        # n
        # n
        numSet = set(nums)
        longest = 0 

        for n in nums:
            # check for start sequence:
            if (n-1) not in numSet:
                length = 0 
                while(n+length) in numSet:
                    length+=1
                longest = max(length,longest)

        return longest
