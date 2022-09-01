
# Problem Link: https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        special_cases = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        answer = 0
        index = 0

        # Iterate over the string
        while index < len(s):

            # Always find 2 characters of the string, in the last one this will become only 1 character
            two_characters = s[index:index + 2]

            # If the 2 characters are in the special_cases dictionary then pick up the value
            if two_characters in special_cases:
                answer += special_cases[two_characters]
                index += 2

            # If not then pick up the second character
            else:
                answer += values[s[index]]
                index += 1

        return answer






