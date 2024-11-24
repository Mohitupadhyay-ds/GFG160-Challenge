class Solution:
    def maximumProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

# Example usage:
prices = [7, 6, 4, 3, 1]
solution = Solution()
print("Maximum profit:", solution.maximumProfit(prices))
