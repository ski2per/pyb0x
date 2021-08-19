from typing import List


class Solution:
    """
    整数反转
    
    给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
    如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
    假设环境不允许存储 64 位整数（有符号或无符号）。
    """
    def reverseInt(self, x: int) -> int:
        r = 0
        if x < 0:
            r = 0-int(str(abs(x))[::-1])
        else:
            r = int(str(x)[::-1])

        if abs(r) > 2**31 - 1:
            return 0
        return r




if __name__ == "__main__":
    # i = 123
    # i = 1534236469
    # i = -123
    i = -2147483648
    sol = Solution()
    print(sol.reverseInt(i))
