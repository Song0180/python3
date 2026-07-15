class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_profit(self, prices: list[int]) -> int:
        profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(prices[r] - prices[l], profit)
                # continue to check next sell
                r += 1
            else:
                # buy again with a cheaper price
                l = r
                r += 1

        return profit
