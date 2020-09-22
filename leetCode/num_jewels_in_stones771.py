# coding=utf-8

class NumJewelsInStones(object):
    def numJewelsInStones(self, J, S):
        sum_jewels = 0
        for str_item in J:
            sum_jewels = sum_jewels + S.count(str_item)
        return sum_jewels
