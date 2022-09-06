# Problem Link: https://leetcode.com/problems/length-of-last-word/submissions/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        letter_index, space_index = None, -1
        index = len(s) - 1

        while index >= 0:

            if s[index].isalpha():

                if not letter_index:
                    letter_index = index

            elif letter_index is not None:
                space_index = index
                break

            index -= 1

        return letter_index - space_index
