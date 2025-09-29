class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return prices[0]

        Maxprofit = 0
        l = 0
        r = 1
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                #check if its the biggest profit
                if Maxprofit < profit:
                    Maxprofit = profit

            else:
                l = r
            
            r += 1
        return Maxprofit
    

# Solution 2: i kinda like this one
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #check if the list is empty
        if len(prices) < 2:
            return 0

        minprice = float('inf') #set a random value for profit
        maxprofit = 0 #counter for profit

        #iterate over every number once
        for num in prices:
            #check if the number is less than the minprice
            if num < minprice:
                minprice = num
            #check if the number is greater than the min
            elif num > minprice:
                maxprofit = max(maxprofit, (num-minprice))
        
        return maxprofit