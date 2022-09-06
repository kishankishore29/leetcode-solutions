# Problem Link: https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digit, carry = 0, 1
        index = len(digits) - 1

        while index >= 0:

            total = digits[index] + carry
            carry = total // 10

            digits[index] = total % 10

            if not carry:
                return digits

            index -= 1

        return [1] + digits



