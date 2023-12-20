from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        list_str_len = len(strs[0])
        list_str = strs[0]
        i = 0
        while i < list_str_len:
            prefix_str = list_str[0:i + 1]
            for j, s in enumerate(strs):
                if i > len(s) or prefix_str != s[0:i + 1]:
                    return list_str[0:i]
            i = i + 1
        return list_str[0:i]
