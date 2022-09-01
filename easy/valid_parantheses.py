# Problem Link: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        index = 0

        for letter in s:
            if letter in ["(", "[", "{"]:
                stack.append(s[index])

            elif letter == ")":

                if stack and stack[-1] == "(":
                    stack.pop()

                else:
                    return False

            elif letter == "]":

                if stack and stack[-1] == "[":
                    stack.pop()

                else:
                    return False

            elif letter == "}":

                if stack and stack[-1] == "{":
                    stack.pop()

                else:
                    return False

            index += 1

        return not stack
