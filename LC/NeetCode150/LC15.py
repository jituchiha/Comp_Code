class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute Force 
        # 3 for loops to find the exact sum match 
        # n^3
        # n
        # tle

        # result = set()
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 if i!=j and i!=k and j!=k:
        #                     result.add(tuple(sorted([nums[i],nums[j],nums[k]])))


                        
        # return list(result)


        # Optimized 
        # Sort the list and then use two pointer approach 
        # n^2
        # n
        # ac

        res = [] 
        nums.sort()

        for i,val in enumerate(nums):
            if i>0 and nums[i-1] == val:
                continue

            left,right = i + 1, len(nums) -1

            while left<right:
                Tsum = val + nums[left] + nums[right]

                if Tsum>0:
                    right-=1

                elif Tsum<0:
                    left+=1

                else:
                    res.append([val,nums[left],nums[right]])
                    left+=1
                    while nums[left] == nums[left -1] and left<right:
                        left+=1
        
        return res

        