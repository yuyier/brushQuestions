from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        list_len = len(nums)
        if list_len == 3:
            sum_near_target = nums[0] + nums[1] + nums[2]
            return sum_near_target
        nums.sort()

        for i in range(list_len):
            first_num_index = i
            left_index = 1 + 1
            right_index = list_len - 1
            while left_index < right_index:
                three_sum = nums[first_num_index] + nums[left_index] + nums[right_index]
                if three_sum == target:
                    return three_sum
                elif three_sum < target:
                    left_index = left_index + 1
                else:
                    right_index = right_index - 1

            # three_sum = nums[first_num_index] + nums[left_index] + nums[right_index]
            # while three_sum < target and left_index < right_index:
            #     left_index = left_index + 1
            #     three_sum = nums[first_num_index] + nums[left_index] + nums[right_index]

        # i = 0
        #
        # while sum_near_target < target:
        #     i = i + 1
        #     if i < list_len - 2:
        #         sum_near_target = nums[i] + nums[i + 1] + nums[i + 2]
        #     else:
        #         break
        # if sum_near_target <= target:
        #     return sum_near_target
        # upper_target = sum_near_target - target
        # lower_target = target - (nums[i - 1] + nums[i] + nums[i + 1])
        # if upper_target < lower_target:
        #     return sum_near_target
        # return nums[i - 1] + nums[i] + nums[i + 1]
