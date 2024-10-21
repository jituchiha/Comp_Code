class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force
        # Go through all of the prices and then decide which one is the right time to buy and sell the stock
        # n^2
        # 1 
        # tle

        # max_price = 0 

        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         max_price= max(max_price,prices[j]-prices[i])

        # return max_price
        

        #Optimized
        # We can implement a one pass solution where we will keep track of lowest price and check if it has the max stock profit with it.
        # n 
        # 1 
        # ac

        min_price = float('inf')
        max_profit = 0


        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)


        return max_profit


        