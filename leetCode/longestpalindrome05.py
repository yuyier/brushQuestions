class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_sub_str = s[0:1]
        s_len = len(s)
        if s_len == 1:
            return s
        for i in range(s_len):
            j1 = i - 1
            j2 = i + 1
            max_sub_str1 = self.getMaxSubStr(j1, j2, s)
            if len(max_sub_str1) > len(max_sub_str):
                max_sub_str = max_sub_str1
            j3 = i
            j4 = i + 1
            max_sub_str2 = self.getMaxSubStr(j3, j4, s)
            if len(max_sub_str2) > len(max_sub_str):
                max_sub_str = max_sub_str2
        return max_sub_str

    def getMaxSubStr(self, index1: int, index2: int, s: str) -> str:
        while index1 >= 0 and index2 < len(s) and s[index1] == s[index2]:
            index1 = index1 - 1
            index2 = index2 + 1

        return s[index1+1:index2-1]
