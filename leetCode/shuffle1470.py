# coding=utf-8

class Shuffle(object):
    def shuffle(self, nums, n):
        new_list = []
        i = 0
        j = n
        while i < n and j < 2 * n:
            new_list.append(nums[i])
            new_list.append(nums[j])
            i = i + 1
            j = j + 1

        return new_list
