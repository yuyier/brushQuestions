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
    def find_median_sorted_arrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        pass

    def find_median(self, nums1, nums2, s1, e1, s2, e2):
        if e1 - s1 < 2:
            if e2 - s2 < 2:
                pass
            else:
                pass
        m1 = self.get_median(nums1, s1, e1)
        m2 = self.get_median(nums2, s2, e2)
        if m1 == m2:
            return m1
        if m1 < m2:
            return self.find_median(self, nums1, nums2, int((s1 + e1) / 2), e1, s2, (e2 - int((e1 - s1) / 2)))

    def get_median(self, nums, s, e):
        return (nums[int((e + s) / 2)] + nums[int((e + s + 1) / 2)]) / 2.0 if (e - s) % 2 else nums[int((e + s) / 2)]


if __name__ == '__main__':
    fm = FindMedianSortedArrays()
    nums = [1, 2, 5]
    m = fm.get_median(nums, 0, len(nums) - 1)
    print(m)
    e2 = 5
    e1 = 3
    s1 = 2
    a = (e2 - int((e1 - s1) / 2))
