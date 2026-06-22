class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=left+1
        max_profit=0

        while right<len(prices):
            profit=prices[right]-prices[left]

            if profit<0:
                left=right
                right=right+1
            else:
                max_profit=max(max_profit,profit)
                
                right=right+1
        
        return max_profit

        