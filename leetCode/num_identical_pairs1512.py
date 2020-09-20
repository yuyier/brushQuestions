# coding=utf-8

class NumIdenticalPairs(object):
    def numIdenticalPairs(self, nums):
        dict_num = {}
        sum_num = 0
        for num in nums:
            if dict_num.__contains__(num):
                dict_num[num] = dict_num[num] + 1
            else:
                dict_num[num] = 1
        for i in dict_num:
            if dict_num[i] > 1:
                sum_num = sum_num + self.add_sum(dict_num[i] - 1)
        return sum_num

    def add_sum(self, val):
        if val == 1:
            sum_num = val
        else:
            sum_num = int((1 + val) * val / 2)

        return sum_num
