# Problem Link: https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = ""

        index_a, index_b, carry = len(a) - 1, len(b) - 1, 0

        while index_a >= 0 or index_b >= 0:
            current_sum = int(a[index_a] if index_a >= 0 else 0) + int(b[index_b] if index_b >= 0 else 0) + carry
            carry, digit = divmod(current_sum, 2)

            answer = str(digit) + answer
            index_a -= 1
            index_b -= 1

        if carry:
            answer = str(carry) + answer

        return answer
