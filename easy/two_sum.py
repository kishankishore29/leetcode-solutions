from typing import List

# Question Link: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create a map to store the index of the numbers in the nums list
        index_map = {}

        # Iterate over the list
        for index, value in enumerate(nums):

            # This is what we want in the map
            required = target - value

            # If the number is present in the map, return its index.
            if required in index_map:
                return [index, index_map[required]]

            # Store the right most index of the number. This will also handle [2, 2] with target 4
            # The first will be stored in the list and then when we arrive the second 2, we will find the first 2 in
            # the list and return the index of the second and first 2
            # THis is possible because we know that there is exactly one solution for the problem other wise we would
            # have to store all the indices of the number
            index_map[value] = index
