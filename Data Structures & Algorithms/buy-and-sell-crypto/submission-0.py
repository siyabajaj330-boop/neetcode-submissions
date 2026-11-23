class Solution:
    def maxProfit(self, prices: List[int]) -> int:

       # we want to parse through the array, treating each day as a
       # potential sell day, 
       # and calculating its potential profit
       # with the minimum day seen so far before it.

       minBuyPriceSoFar = prices[0]
       maxProfit = -1

       for sellPrice in prices:
            currProfit = sellPrice - minBuyPriceSoFar
            maxProfit = max(maxProfit, currProfit)
            minBuyPriceSoFar = min(minBuyPriceSoFar, sellPrice)

       return maxProfit 






            

        

        