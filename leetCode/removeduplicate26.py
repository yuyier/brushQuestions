from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for index, list_num in enumerate(nums):
            num_count = nums.count(list_num)
            if num_count > 1:
                del nums[index:index + num_count - 1]
        return len(nums)
