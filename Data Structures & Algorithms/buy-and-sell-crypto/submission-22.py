class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l,r=0,1 # left BUY and right sell

        max_profit= 0

        while r<len(prices):
            profit=prices[r]-prices[l]
            print("buy : {} sell: {} profit : {}".format(l,r,profit))

            if prices[r] > prices[l]:
                max_profit=max(profit,max_profit)
            else:
                l=r
            r +=1
        
        return max_profit


