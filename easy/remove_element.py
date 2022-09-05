# Problem Link: https://leetcode.com/problems/remove-element/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0

        while fast < len(nums):
            if val != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        return slow
