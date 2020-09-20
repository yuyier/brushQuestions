# coding=utf-8

class SumOddLengthSubarrays(object):
    def sumOddLengthSubarrays(self, arr):
        arr_len = len(arr)
        i = 1
        sum_all = 0
        while i <= arr_len:
            sum_all = sum_all + self.add_sum(arr, i)
            i = i + 2

        return sum_all

    def add_sum(self, arr, nums):
        arr_len = len(arr)
        sum_all = 0
        for i in range(arr_len):
            j = i
            num = nums
            if (j + nums - 1) < arr_len:
                while num > 0:
                    sum_all = sum_all + arr[j]
                    j = j + 1
                    num = num - 1

            else:
                break

        return sum_all
