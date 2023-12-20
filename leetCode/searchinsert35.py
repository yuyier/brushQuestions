from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        for index_num in nums:
            if index_num < target:
                continue
            else:
                return nums.index(index_num)
        return nums.index(index_num)+1
