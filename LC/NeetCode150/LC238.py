class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force
        # Compute the product for each element except the self and then return the updated list
        # n^2
        # n
        # tle
        # res = []
        # for i in range(len(nums)):
        #     mul = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         mul*=nums[j]
        #     res.append(mul)

        # return res 

        # Optimized approach
        # Using Prefix and Suffix product for the first pass we will compute the prefix product and then for the next one we would be computing the suffix prod and then simply return the result as the array is populated with the required product 
        # n 
        # n
        # ac


        n = len(nums)

        ans = [1]*n

        prefix =1 
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
        #print(ans)
        suffix = 1
        for i in range(n-1,-1,-1):
            ans[i]*=suffix
            suffix *=nums[i]

        return ans 