from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_len = len(nums)
        while k > num_len:
            k = k - num_len
        if k == num_len:
            return nums
        nums.reverse()
        front_half_start, front_half_end = 0, k - 1
        back_half_start, back_half_end = k, num_len - 1
        self.rotateOperation(front_half_start, front_half_end, nums)
        self.rotateOperation(back_half_start, back_half_end, nums)
        return nums

    def rotateOperation(self, start_index, end_index, nums):
        while start_index < end_index:
            num = nums[start_index]
            nums[start_index], nums[end_index] = nums[end_index], num
            start_index, end_index = start_index + 1, end_index - 1


if __name__ == "__main__":
    # nums = [1, 2, 3, 4, 5, 6, 7]
    # k = 3
    # nums = [-1, -100, 3, 99]
    # k = 2
    nums =[-1]
    k=2
    print(Solution().rotate(nums, k))
    # print(nums)
