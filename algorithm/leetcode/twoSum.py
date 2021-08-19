from typing import List


class Solution:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for idx, num in enumerate(nums):
            remainder = target - num
            for x in range(idx+1, n):
                if nums[x] == remainder:
                    return [idx, x]

    def twoSum2(self, nums:List[int], target: str) -> list:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for idx, num in enumerate(nums):
            key = target - num
            if key in d:
                return [idx, d[key]] 
            d[num] = idx
        return []




if __name__ == '__main__':
    # sol = Solution()
    # print(sol.twoSum([3, 7, 8, 10, 4, 5], 9))

    sol = Solution()
    print(sol.twoSum2([3, 7, 8, 10, 4, 5], 9))

