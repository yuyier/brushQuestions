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
    def mediaIndex(self, len_num, nums, pre_index2, last_index2):
        if len_num <= 1:
            index = pre_index2
        else:
            index = int(len_num / 2) + pre_index2
        media_num = nums[index]
        return index, media_num

    def mediaTupleIndex(self, len_num, nums, pre_index2, last_index2):
        if len_num <= 2:
            index1 = pre_index2
            index2 = last_index2
        else:
            index1 = int(len_num / 2) + pre_index2 - 1
            index2 = index1 + 1
        media_nums = (nums[index1] + nums[index2]) / 2
        # media_nums = nums[index1]
        return index1, media_nums

    def newIndex(self, media_nums1, media_nums2, index1, pre_index1, last_index1, pre_index2, last_index2):
        if media_nums1 < media_nums2:
            index_len = index1 - pre_index1
            pre_index1 = index1
            last_index1 = last_index1
            pre_index2 = pre_index2
            last_index2 = last_index2 - index_len
        else:
            index_len = last_index1 - index1
            pre_index1 = pre_index1
            last_index1 = index1
            pre_index2 = pre_index2 + index_len
            last_index2 = last_index2

        return pre_index1, last_index1, pre_index2, last_index2
        # pass

    def returnMediaNum(self, len2, nums1, nums2, pre_index1, last_index1, pre_index2, last_index2):
        if len2 % 2 == 0:
            index, median_num = self.mediaTupleIndex(len2, nums2, pre_index2, last_index2)
            if nums2[index] <= nums1[pre_index1] <= nums2[index + 1]:
                return nums1[pre_index1]
            elif nums1[pre_index1] < nums2[index]:
                return nums2[index]
            else:
                return nums2[index + 1]
        else:
            index, median_num = self.mediaIndex(len2, nums2, pre_index2, last_index2)
            if nums2[index - 1] <= nums1[pre_index1] <= nums2[index + 1]:
                return (nums1[pre_index1] + nums2[index]) / 2
            elif nums1[pre_index1] < nums2[index - 1]:
                return (nums2[index - 1] + nums2[index]) / 2
            else:
                return (nums2[index + 1] + nums2[index]) / 2

        # pass

    def lenTwoIndex(self, nums1, nums2, pre_index1, last_index1, pre_index2, last_index2):
        media_num = -1
        if nums1[pre_index1] < nums2[pre_index2] and nums1[last_index1] < nums2[last_index2]:
            pre_index1 = last_index1
            last_index1 = last_index1
            pre_index2 = pre_index2
            last_index2 = last_index2 - 1
            # else:
        #     pass
        elif nums1[last_index1] > nums2[last_index2] and nums1[pre_index1] > nums2[pre_index2]:
            pre_index1 = pre_index1
            last_index1 = pre_index1
            pre_index2 = pre_index2 + 1
            last_index2 = last_index2

        elif nums1[pre_index1] > nums2[pre_index2] and nums1[last_index1] < nums2[last_index2]:
            pre_index1 = pre_index1
            last_index1 = last_index1
            pre_index2 = pre_index2 + 1
            last_index2 = last_index2 - 1
        else:
            len_num = last_index2 + 1 - pre_index2
            if len % 2 == 0:
                index, media_num = self.mediaTupleIndex(self, len_num, nums2, pre_index2, last_index2)
            else:
                index, media_num = self.mediaIndex(self, len_num, nums2, pre_index2, last_index2)

            pass
        return pre_index1, last_index1, pre_index2, last_index2, media_num

    def mediaNum(self, pre_index1, last_index1, pre_index2, last_index2, nums1, nums2):
        len1 = last_index1 + 1 - pre_index1
        len2 = last_index2 + 1 - pre_index2
        if len1 == 1 and len2 == 1:
            return (nums1[pre_index1] + nums2[pre_index2]) / 2
        elif len1 == 1:
            return self.returnMediaNum(len2, nums1, nums2, pre_index1, last_index1, pre_index2, last_index2)
        elif len2 == 1:
            return self.returnMediaNum(len1, nums2, nums1, pre_index2, last_index2, pre_index1, last_index1)
        elif len1 == 2:
            if nums1[0] < nums2[pre_index2] and nums1[1] > nums2[last_index2] and len2 % 2 == 0:
                index, media_num = self.mediaTupleIndex(len2, nums2, pre_index2, last_index2)
                return media_num
            elif nums1[0] < nums2[pre_index2] and nums1[1] > nums2[last_index2] and len2 % 2 != 0:
                index, media_num = self.mediaIndex(len2, nums2, pre_index2, last_index2)
                return media_num
            else:
                pre_index1, last_index1, pre_index2, last_index2, media_num = self.lenTwoIndex(nums1, nums2, pre_index1,
                                                                                               last_index1, pre_index2,
                                                                                               last_index2)
                if media_num > 0:
                    return media_num
                len2 = last_index2 + 1 - pre_index2
                len1 = last_index1 + 1 - pre_index1

        elif len2 == 2:
            if nums2[0] < nums1[pre_index1] and nums2[1] > nums1[last_index1] and len1 % 2 == 0:
                index, media_num = self.mediaTupleIndex(len1, nums1, pre_index1, last_index1)
                return media_num
            elif nums2[0] < nums1[pre_index1] and nums2[1] > nums1[last_index1] and len1 % 2 != 0:
                index, media_num = self.mediaIndex(len1, nums1, pre_index1, last_index1)
                return media_num
            else:
                pre_index2, last_index2, pre_index1, last_index1, media_num = self.lenTwoIndex(nums2, nums1, pre_index2,
                                                                                               last_index2, pre_index1,
                                                                                               last_index1)
                if media_num > 0:
                    return media_num
                len1 = last_index1 + 1 - pre_index1
                len2 = last_index2 + 1 - pre_index2
        else:

            if len1 % 2 == 0:
                index1, media_nums1 = self.mediaTupleIndex(len1, nums1, pre_index1, last_index1)
            else:
                index1, media_nums1 = self.mediaIndex(len1, nums1, pre_index1, last_index1)
            if len2 % 2 == 0:
                index2, media_nums2 = self.mediaTupleIndex(len2, nums2, pre_index2, last_index2)
            else:
                index2, media_nums2 = self.mediaIndex(len2, nums2, pre_index2, last_index2)
            if len1 < len2:
                pre_index1, last_index1, pre_index2, last_index2 = self.newIndex(media_nums1, media_nums2, index1,
                                                                                 pre_index1, last_index1, pre_index2,
                                                                                 last_index2)
            else:
                pre_index2, last_index2, pre_index1, last_index1 = self.newIndex(media_nums2, media_nums1, index2,
                                                                                 pre_index2, last_index2, pre_index1,
                                                                                 last_index1)

        return self.mediaNum(pre_index1, last_index1, pre_index2, last_index2, nums1, nums2)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        pre_index1 = 0
        last_index1 = len(nums1) - 1
        pre_index2 = 0
        last_index2 = len(nums2) - 1
        return self.mediaNum(pre_index1, last_index1, pre_index2, last_index2, nums1, nums2)

        # assert type(reps1) == type(reps2), "type: '{}' != '{}'".format(type(reps1), type(reps2))
        # pass
