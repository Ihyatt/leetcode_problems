
# time: O(n)
# space:O(1)
# Best Time to Buy and Sell Stock

"""
[7,1,5,3,6,4]
max_profit = 5
profit = 5
min_price = 1


"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit, profit = 0, 0 
        min_price = prices[0]
        for price in prices:
            if price < min_price: #keep locating the min price
                min_price = price
                continue
            profit = price - min_price #price - min_price
            if profit > max_profit: #locate max profit
                max_profit = profit
        return max_profit