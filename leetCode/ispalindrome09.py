class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        i = 0
        j = len(str_x) - 1
        while i <= j:
            if str_x[i] != str_x[j]:
                return False
            else:
                i = i + 1
                j = j - 1
        return True
