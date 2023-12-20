from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_len = len(nums1)
        if nums1 == 0:
            return nums2
        if nums1_len == m:
            return nums1
        i, j = 0, 0
        while i < nums1_len:
            if i < m and nums1[i] > nums2[j]:
                temp_num, nums1[i] = nums1[i], nums2[j]
                nums2[j] = temp_num
                nums2.sort()
            elif i >= m:
                nums1[i] = nums2[j]
                j += 1
            i += 1
        return nums1
