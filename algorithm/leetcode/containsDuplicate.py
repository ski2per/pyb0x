from typing import List

class Solution:
    """
    存在重复元素

    给定一个整数数组，判断是否存在重复元素。
    如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for x in nums:
            d[x] = 0
        print(d)
        return len(d.keys()) != len(nums)


if __name__ == '__main__':
    # l = [1,1,1,3,3,4,3,2,4,2]
    l = [1,2,3,1]
    sol = Solution()
    print(sol.containsDuplicate(l))
