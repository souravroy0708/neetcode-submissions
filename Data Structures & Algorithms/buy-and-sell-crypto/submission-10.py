class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        left,right=0,1 
        # left is buying proce
        #right is selling proce

        while right<len(prices):
            print("left : {} right : {}".format(left,right))
            
            
            if prices[left]<prices[right]:
                profit=prices[right]-prices[left]
                max_profit=max(max_profit,profit) 
                print("profit : {} max_profit:{}".format(profit,max_profit))    
            else:
                left = right
            right = right +1
        return max_profit

        