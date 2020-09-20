# coding=utf-8
class RunningSum(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_len = len(nums)
        new_list = []
        sum = 0
        for i in range(num_len):
            sum = sum + nums[i]
            new_list.append(sum)
        return new_list
