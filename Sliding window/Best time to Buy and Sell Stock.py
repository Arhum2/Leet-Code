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