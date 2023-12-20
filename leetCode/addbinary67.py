class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = str(int(a) + int(b))
        c1 = c[::-1]
        add_num = 0
        for index, num in enumerate(c1):
            if int(num) + add_num > 1:
                c1 = c1[0:index]+(str((int(num) + add_num) % 2)) + c1[index + 1:]
                add_num = 1
            else:
                c1 = c1[0:index] + (str((int(num) + add_num))) + c1[index + 1:]
                add_num = 0
        return "1" + c1[::-1] if add_num > 0 else c1[::-1]
