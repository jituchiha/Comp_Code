class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force
        # Check for all the pairs that we can think of and see if the sum makes up to the target.
        # TC: O(N^2)
        # SC: O(1)
        # AC

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

        return -1

        # Optimized Sol
        # Trick here is x+y = target that means x = target - y so we can effectively just check for the complement or the RHS of our equation with the elements of the array. And how can we get the indices then? We will be storing them in the hashmap to retrive them when we get a match
        # TC: O(N)
        # SC: O(N)
        # AC

        hm = {}

        for i in range(len(nums)):
            comp = target - nums[i] 

            if comp in hm:
                return [i,hm[comp]]

            hm[comp] = i

        return -1


        
        