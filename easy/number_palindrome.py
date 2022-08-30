# Question Link: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative number are not allowed
        if x < 0:
            return False

        new_number = 0
        old_number = x

        # We will create a new_number with the following technique:
        # number = number * 10 + last_digit_of_old_number
        # 1234 = (10 * 10 * 10 * 1) + (10 * 10 * 2) + (10 * 3) + 4
        # Extract last digit of old_number and create left most digit of new number: 4 + 0 * 10 = 4
        # Extract second last digit of old_number and create second left most digit of new number: 4 * 10 + 3 = 43
        # If we carry on for 2 more steps then we get 4321
        while old_number:
            digit = old_number % 10
            new_number = new_number * 10 + digit

            old_number //= 10

        return x == new_number
