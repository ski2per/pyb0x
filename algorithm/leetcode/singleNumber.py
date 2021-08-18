from typing import List


class Solution:
    """
    只出现一次的数字

    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
    """
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for x in nums:
            result ^= x
            print(result)
        return result


if __name__ == '__main__':
    l = [4, 1, 2, 1, 2]
    sol = Solution()
    print(sol.singleNumber(l))
