
''''
给定一个整数数组nums和一个整数目标值target，请你在该数组中找出和为目标值target的那两个
整数，并返回它们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。



示例
1：

输入：nums = [2, 7, 11, 15], target = 9
输出：[0, 1]
解释：因为
nums[0] + nums[1] == 9 ，返回[0, 1] 。
示例
2：

输入：nums = [3, 2, 4], target = 6
输出：[1, 2]
示例
3：

输入：nums = [3, 3], target = 6
输出：[0, 1]
'''



from typing import List

class AddTwoNumbers01:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_list=[]
        for item in nums:
            another_num=target-item
            item_index = nums.index(item)
            if another_num in nums[item_index+1:]:
                another_num_index = nums[item_index+1:].index(another_num)+item_index+1
                result_list.append(item_index)
                result_list.append(another_num_index)
                return result_list

        return result_list

