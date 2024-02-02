from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        pre_jump_index_step = temp_jump_index_step = jump_node = 0
        for index, step in enumerate(nums):
            index_step = step + index
            if index > pre_jump_index_step:
                pre_jump_index_step = temp_jump_index_step
                jump_node = jump_node + 1
            if index <= pre_jump_index_step and index_step > pre_jump_index_step and index_step > temp_jump_index_step:
                temp_jump_index_step = index_step
        return jump_node


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    # nums = [2, 3, 0, 1, 4]
    # nums =[0]
    # nums = [2,1]
    # nums = [2,3, 1]
    nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
    print(Solution().jump(nums))
