class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        curr_val = prices[0]

        for i in range(1, len(prices)):
            if (prices[i] - curr_val) > 0:
                profit += (prices[i] - curr_val)
                curr_val = prices[i]
            else:
                curr_val = prices[i]
        return profit
             

        