class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Optimized 
        # We can run binary search to find the optimal eating speed and the way we are going to do that is by simulating the number of hours koko takes to eat and it's going to be equal to banana pile/ k
        # p*log(max(p))
        # 1

        l,r = 1, max(piles)
        res = r 

        while l<=r:
            mid = (l + r )//2

            hours = 0 
            for p in piles:
                hours+= math.ceil(p/mid)

            if hours <= h:
                res = min(res,mid)

                r = mid - 1

            else:
                l = mid + 1

        return res

        