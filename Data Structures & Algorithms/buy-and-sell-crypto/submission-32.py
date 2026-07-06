class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left =0 # left is buy price index
        right = 1 # right is selling price index

        max_profit = 0

        for i in range(1,len(prices)):

            profit = prices[right]  - prices[left]
            print(f" profit : {profit} max_profit : {max_profit} left : {left} right : {right} ")
            max_profit = max(max_profit,profit)

            if prices[left] > prices[right]:
                left = right

            right += 1
        
        return max_profit

        