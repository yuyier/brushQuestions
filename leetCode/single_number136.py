from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        return res


if __name__ == "__main__":
    nums = [2, 2, 1]
    nums = [4, 1, 2, 1, 2]
    nums = [1]
    nums = [1,1,3,3,0]
    print(Solution().singleNumber(nums))
