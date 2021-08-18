from typing import List


class Solution:
    """
    删除排序数组中的重复项

    给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
    不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1

if __name__ == '__main__':
    l = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(l.pop(3))
    print(l)
    sol = Solution()
    print(sol.removeDuplicates(l))
