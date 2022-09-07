# Problem Link: https://leetcode.com/problems/search-insert-position/
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end, index = 0, len(nums) - 1, 0

        while start <= end:

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                start = mid + 1
                index = mid + 1

            else:
                end = mid - 1

        return index




