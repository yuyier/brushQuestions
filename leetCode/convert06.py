# coding=UTF-8
'''
# 用例
# 1、一个完整的Z型
# 2、不完整的Z型
# 3、空字符串
# 4、长度小于rowNums
# 5、列头指向的位置！=列尾指向的位置
# 6、下一个列头指向的位置！=列尾指向的位置
# 7、rowNums==1的情况
'''
class Convert(object):
    def convert(self, s, numRows):
        str_len = len(s)
        if numRows == 1 or str_len <= numRows:
            return s
        colum_nums = 2 * numRows - 2
        # 所有的数据分列
        if str_len % colum_nums == 0:
            column = int(str_len / colum_nums)
        else:
            column = int(str_len / colum_nums) + 1
        new_str = ''
        for i in range(numRows):
            step = colum_nums
            for j in range(column):
                # 列的末端
                column_end = (j + 1) * step - i
                str_step = i + j * step
                if str_step < str_len:
                    if column_end > str_len - 1 or str_step == column_end or i + (j + 1) * step == column_end:
                        new_str = new_str + s[str_step]
                    else:
                        new_str = new_str + s[str_step] + s[column_end]

        return new_str

# L E C D
# E T O E

# 用例
# 1、一个完整的Z型
# 2、不完整的Z型
# 3、空字符串
# 4、长度小于rowNums
# 5、列头指向的位置！=列尾指向的位置
# 6、下一个列头指向的位置！=列尾指向的位置
# 7、rowNums==1的情况
