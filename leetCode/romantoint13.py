class Solution:
    def romanToInt(self, s: str) -> int:
        dict_roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40,
                      "XC": 90, "CD": 400, "CM": 900}
        int_num = 0
        s_len = len(s)
        i = 0
        j = 1
        while j < s_len:
            if s[i:j + 1] in dict_roman:
                int_num = int_num + dict_roman[s[i:j + 1]]
                i = i + 2
                j = j + 2
            else:
                int_num = int_num + dict_roman[s[i]]
                i = i + 1
                j = j + 1
        if i < s_len:
            int_num = int_num + dict_roman[s[i]]
        return int_num
