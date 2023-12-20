from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len <= 2:
            return max(nums)
        return max(self.max_rob(nums[:nums_len - 1]), self.max_rob(nums[1:]))

    def max_rob(self, nums_list: List[int]) -> int:
        pre, cur = 0, 0
        for num in nums_list:
            cur, pre = max(cur, pre + num), cur
        return cur
        # nums_len = len(nums_list)
        # if nums_len <= 2:
        #     return max(nums_list)
        # max_rob = []
        # max_rob.append(nums_list[0])
        # max_rob.append(max(nums_list[0], nums_list[1]))
        # pre = 0
        # cur = 1
        # for num in nums_list[2:]:
        #     max_rob.append(max(max_rob[cur], max_rob[pre] + num))
        #     pre = cur
        #     cur = cur + 1
        # return max(max_rob)
