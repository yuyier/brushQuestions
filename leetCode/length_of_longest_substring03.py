# coding=UTF-8
'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_str = ''
        max_len = 0
        next_index = 0
        str_len = 0
        while next_index < len(s):
            if s[next_index] not in max_str:
                max_str = max_str + s[next_index]
                str_len = str_len + 1
                next_index = next_index + 1
            else:
                if str_len > max_len:
                    max_len = str_len
                index = max_str.index(s[next_index])
                pre = index + 1
                max_str = max_str[pre:] + s[next_index]
                next_index = next_index + 1
                str_len = len(max_str)
        if str_len > max_len:
            max_len = str_len
        return max_len
