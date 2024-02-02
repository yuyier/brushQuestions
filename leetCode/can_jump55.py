from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index, max_step = len(nums) - 1, 0
        for jump_index, jum_step in enumerate(nums):
            position = jum_step + jump_index
            if jump_index <= max_step and  position > max_step:
                max_step = position

        return max_step >= last_index


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    # nums = [3, 2, 2, 0, 4]
    # nums = [2, 3]
    # nums = [3, 0, 0, 1,0, 4]
    # nums = [0, 3, 1, 1, 4]
    # nums = [3, 1, 0, 1, 2, 1, 1, 4]
    # nums =[0]

    print(Solution().canJump(nums))
