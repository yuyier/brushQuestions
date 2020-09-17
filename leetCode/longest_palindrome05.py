# coding=UTF-8
'''给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


class LongestPalindrome(object):
    def longest_palindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_len = len(s)
        if str_len % 2 == 0:
            left_mid = int(str_len / 2) - 1
        else:
            left_mid = int(str_len / 2)
        right_mid = left_mid
        max_len = 0
        max_start = 0
        max_end = 0

        while left_mid > 0 or right_mid < str_len:

            # aba
            if (left_mid - 1) >= 0 and (left_mid + 1) < str_len and s[left_mid - 1] == s[left_mid + 1]:
                left_point1 = left_mid - 1
                right_point1 = left_mid + 1
                now_len = 1
                if max_len < 2 * left_mid:
                    max_len, max_start, max_end = self.get_max(left_point1, right_point1, max_len,
                                                               max_start,
                                                               max_end, now_len, str_len, s)
            # aba
            if left_mid != right_mid and (right_mid - 1) >= 0 and (right_mid + 1) < str_len and s[right_mid - 1] == s[
                right_mid + 1]:
                left_point2 = right_mid - 1
                right_point2 = right_mid + 1
                now_len = 1
                if max_len < 2 * (str_len - right_mid):
                    max_len, max_start, max_end = self.get_max(left_point2, right_point2, max_len,
                                                               max_start,
                                                               max_end, now_len, str_len, s)
            # aa
            if (left_mid - 1) >= 0 and s[left_mid - 1] == s[left_mid]:
                left_point1 = left_mid - 1
                right_point1 = left_mid
                now_len = 0
                if max_len < 2 * left_mid:
                    max_len, max_start, max_end = self.get_max(left_point1, right_point1, max_len,
                                                               max_start,
                                                               max_end, now_len, str_len, s)
            # aa
            if (right_mid + 1) < str_len and s[right_mid] == s[right_mid + 1]:
                left_point2 = right_mid
                right_point2 = right_mid + 1
                now_len = 0
                if max_len < 2 * (str_len - right_mid):
                    max_len, max_start, max_end = self.get_max(left_point2, right_point2, max_len,
                                                               max_start,
                                                               max_end, now_len, str_len, s)

            left_mid = left_mid - 1
            right_mid = right_mid + 1
        return s[max_start:(max_end + 1)]

    def get_max(self, left_point, right_point, max_len, max_start, max_end, now_len, str_len, s):
        while s[right_point] == s[left_point]:
            now_len = now_len + 2
            start_point = left_point
            end_point = right_point
            if (left_point - 1) >= 0 and (right_point + 1) < str_len:
                left_point = left_point - 1
                right_point = right_point + 1
            else:
                break

        if now_len > max_len:
            max_len = now_len
            max_start = start_point
            max_end = end_point

        return max_len, max_start, max_end
