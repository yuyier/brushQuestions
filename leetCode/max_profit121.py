from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_index, max_profit = len(prices) - 1, 0
        if sell_index == 0:
            return max_profit
        buy_index = sell_index - 1
        while buy_index >= 0:
            if prices[buy_index] > prices[sell_index]:
                sell_index = buy_index
                buy_index = buy_index - 1
            else:
                profit = prices[sell_index] - prices[buy_index]
                max_profit = max(profit,max_profit)
                buy_index = buy_index - 1
        return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    # prices = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(prices))
