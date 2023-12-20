class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s = s.rstrip()
        # s_list =
        # s_list_len=len(s_list)
        return len(s.rstrip().split(" ")[-1])
