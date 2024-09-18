# Day 3



class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        num_strs = [str(num) for num in nums]

        num_strs.sort(key = lambda a:a*10, reverse = True)

        if num_strs[0] == "0":
            return "0"

        return "".join(num_strs)
        