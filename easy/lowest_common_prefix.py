# Problem Link: https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:

        common = ""
        first_string = s[0]

        # Iterate over each of the letter in the first_string
        for index, value in enumerate(first_string):

            # Denotes if all the other words contains the letter
            all_words_contain_letter = True

            # Iterate over all the other words from range 1 to the last word
            for j in range(1, len(s)):
                word = s[j]

                # If the current word has ended or the letters don't match
                if index > len(word) - 1 or word[index] != value:
                    all_words_contain_letter = False
                    break

            # Check the value of the boolean variable
            if all_words_contain_letter:
                common += value
            else:
                break

        return common
