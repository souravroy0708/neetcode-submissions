class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1 # l buy r sell
        max_profit=0
        while r < len(prices):
            current_profit=prices[r]-prices[l]
            max_profit=max(current_profit,max_profit)

            if prices[r] < prices[l]:
                l +=1
            else:
                r +=1
        return max_profit
            

        