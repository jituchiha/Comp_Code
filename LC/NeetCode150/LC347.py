from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute Force
        # Store the frequency of each integer and then based on that store the sorted order based on the frequency and then return the top k elements out. 
        # nlogn
        # n
        # freq = Counter(nums)

        # sorted_ele = sorted(freq, key= lambda x: freq[x], reverse =True )

        # return sorted_ele[:k]

        # Optimized Approach
        # Use min-heap and store all of the elements in the heap and then pop the k largest in them. 
        # nlogk
        # n + k

        #freq = Counter(nums)

        #return heapq.nlargest(k,freq.keys(),key = freq.get)

        # Most Optimized approach
        # Using Bucket Sort to store the most frequent items and then querying it
        # n 
        # n 

        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num,count in freq.items():
            buckets[count].append(num)

        res = []

        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res 

        #print(buckets)
        