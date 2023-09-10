class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_str = 0
        set_list = set()
        sub_str_len = 0
        i = 0
        while i < len(s):
            index = i
            while index < len(s) and set_list.__len__() == sub_str_len:
                set_list.add(s[index])
                sub_str_len += 1
                index += 1

            if set_list.__len__()  > max_str:
                max_str = set_list.__len__()
            set_list.clear()
            sub_str_len = 0
            i += 1

        return max_str
