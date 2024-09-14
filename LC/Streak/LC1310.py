#Day 1

# Brute force 
# Tried to compute xor for each query seperately as mentioned in the question.
# Time Complexity : O(n*q)
# Space Complexity: O(1)
# Verdict: TLE

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        for query in queries:
            i,j = query
            res=0
            for z in range(i,j+1):
                res ^= arr[z]
                
            ans.append(res)


        return ans   
    


# Optimized Version
# Generating a prefix array which stores the prefix xor values of the ranges and then we just have to xor two values to get the result.
# Time Complexity: O(n+q)
# Space Complexity: O(n)
# Verdict: Accepted


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * (n+1)

        for i in range(1, n+1):
            prefix[i] = prefix[i-1]^arr[i-1]
            
        res = []

        for l,r in queries:
            res.append(prefix[l]^prefix[r+1])

        return res



# Best case
# We can save space as well if we edit the main array itself.
# Time Complexity: O(n+q)
# Space Complexity: O(1)
# Verdict: Accepted


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = [] 
        for i in range(1,len(arr)):
            arr[i]^=arr[i-1]    

        for l,r in queries:
            if l>0:
                res.append(arr[l-1]^arr[r])
            else:
                res.append(arr[r])

        return res

        