from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count, max_num = 0, 0
        s = set(nums)
        for num in s:
            num_count = nums.count(num)
            if num_count > max_count:
                max_count, max_num = num_count, num
        return max_num


if __name__ == "__main__":
    nums = [3, 2, 3]
    # nums = [2, 2, 1, 1, 1, 2, 2]
    # nums = [3, 2, 4]
    print(Solution().majorityElement(nums))
