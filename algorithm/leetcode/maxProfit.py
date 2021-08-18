from typing import List


class Solution:
    """
    买卖股票的最佳时机 II

    给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    """
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        for j in range(1, len(prices)):
            if prices[i] < prices[j]:
                p = prices[j] - prices[i]
                profit += p
            i += 1
        return profit


if __name__ == '__main__':
    # l = [7, 1, 5, 3, 6, 4]
    l = [1,2,3,4,5]

    sol = Solution()
    print(sol.maxProfit(l))
