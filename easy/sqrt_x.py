# Problem Link: https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:

        if x in [0, 1]:
            return x

        start, end = 1, x // 2
        answer = 0

        while start <= end:

            mid = (start + end) // 2
            square = mid * mid

            if square == x:
                return mid

            elif square > x:
                end = mid - 1

            else:
                answer = mid
                start = mid + 1

        return answer


