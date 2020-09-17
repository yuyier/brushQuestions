# coding=UTF-8
'''给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

 

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


class FindMedianSortedArrays(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        pre_index1 = 0
        pre_index2 = 0
        len1 = len(nums1)
        len2 = len(nums2)
        last_index1 = len1 - 1
        last_index2 = len2 - 1
        pre_nums = 0
        last_nums = 0
        pre = 0
        last = 0
        while (pre_nums + last_nums) < (len1 + len2):
            if pre_index1 <= last_index1 and pre_index2 <= last_index2:
                if nums1[pre_index1] < nums2[pre_index2]:
                    pre = nums1[pre_index1]
                    pre_index1 = pre_index1 + 1
                    pre_nums = pre_nums + 1
                else:
                    pre = nums2[pre_index2]
                    pre_index2 = pre_index2 + 1
                    pre_nums = pre_nums + 1
                if nums1[last_index1] > nums2[last_index2]:
                    last = nums1[last_index1]
                    last_index1 = last_index1 - 1
                    last_nums = last_nums + 1
                else:
                    last = nums2[last_index2]
                    last_index2 = last_index2 - 1
                    last_nums = last_nums + 1

            elif pre_index1 > last_index1:
                pre = nums2[pre_index2]
                pre_index2 = pre_index2 + 1
                pre_nums = pre_nums + 1
                last = nums2[last_index2]
                last_index2 = last_index2 - 1
                last_nums = last_nums + 1

            elif pre_index2 > last_index2:
                pre = nums1[pre_index1]
                pre_index1 = pre_index1 + 1
                pre_nums = pre_nums + 1
                last = nums1[last_index1]
                last_index1 = last_index1 - 1
                last_nums = last_nums + 1

        if (len1 + len2) % 2 == 0:
            return (pre + last) / 2
        else:
            if pre_nums > last_nums:
                return pre
            else:
                return last

            # pass
