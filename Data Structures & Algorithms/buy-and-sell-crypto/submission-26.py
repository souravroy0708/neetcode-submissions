class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left,right=0,1
        max_profit=0
        while right<len(prices):
            #shell - buy = profit
            profit=prices[right]-prices[left]
            print (" left index {} right index : {}".format(left,right))
            print (" buy : {} sell : {} profit : {}".format(prices[left],prices[right],profit))
            if profit<0:
                left = right
            right +=1

            max_profit=max(max_profit,profit)
        
        return max_profit