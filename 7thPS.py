from typing import List

class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        for i in range(1, len(prices)): #Iterate through the prices
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1] #Profit Calculation
        return max_profit

# Example usage:
prices = [4, 2, 2, 2, 4]
solution = Solution()
print("Maximum profit:", solution.maximumProfit(prices))
