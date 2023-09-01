'''
给你一个下标从0开始的二维整数数组nums 。一开始你的分数为0 。你需要执行以下操作直到矩阵变为空：

矩阵中每一行选取最大的一个数，并删除它。如果一行中有多个最大的数，选择任意一个并删除。
在步骤1
删除的所有数字中找到最大的一个数字，将它添加到你的分数中。
请你返回最后的分数 。


示例1：

输入：nums = [[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]
输出：15
解释：第一步操作中，我们删除7 ，6 ，6和3 ，将分数增加7 。下一步操作中，删除2 ，4 ，5
和2 ，将分数增加5 。最后删除1 ，2 ，3和1 ，将分数增加3 。所以总得分为7 + 5 + 3 = 15 。

示例2：

输入：nums = [[1]]
输出：1
解释：我们删除1并将分数增加1 ，所以返回1 。
'''
from typing import List


class MatrixSum:
    def matrixSum(self, nums: List[List[int]]) -> int:
        maxtrix_sum = 0
        nums_len = len(nums)
        while len(nums[0]) != 0:
            max_list_num = 0
            for i in range(nums_len):
                max_nums = max(nums[i])
                if max_nums > max_list_num:
                    max_list_num = max_nums
                nums[i].remove(max_nums)
            maxtrix_sum += max_list_num

        return maxtrix_sum
