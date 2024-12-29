class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Finds the maximum profit that can be achieved from buying and selling a stock,
        where you must buy before you sell.

        :param prices: List of stock prices, where prices[i] is the price of the stock on day i
        :return: Maximum profit that can be achieved
        """
        # Initialize variables to track maximum profit and the minimum purchase price
        max_profit = 0
        min_purchase = prices[0]

        for price in prices:
            # Update the maximum profit with the higher value between the current max and the profit from this price
            max_profit = max(max_profit, price - min_purchase)
            # Update the minimum purchase price with the lowest value seen so far
            min_purchase = min(min_purchase, price)

        return max_profit