from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums):
            index_count = nums.count(nums[index])
            end = index + index_count
            if index_count > 2:
                start = index + 2
                del nums[start:end]
                index = start
            else:
                index = end
        return nums


if __name__ == "__main__":
    # nums = [1, 1, 1, 2, 2, 3]
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    nums = [1, 1, 1, 2, 2, 2, 3, 3]
    print(Solution().removeDuplicates(nums))
