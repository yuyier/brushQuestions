# coding=UTF-8
'''
用例
1、负数
2、整数
3、反转后数据值范围： [−pow(2，31),  pow(2,31) − 1]
4、返回后小于−pow(2，31)
5、反转后大于pow(2,31) − 1
6、<10的整数
7、<10的负数
8、整数：10，20，-10，-20
'''


class Reverse(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse_x = 0
        flag = False
        pow_num = pow(2, 31)
        max = pow_num - 1
        min = 0 - pow_num
        if x < 0:
            abs_x = abs(x)
            flag = True

        else:
            abs_x = x

        while abs_x > 0:
            reverse_x = reverse_x * 10 + abs_x % 10
            abs_x = int(abs_x / 10)

        if flag:
            reverse_x = 0 - reverse_x
            if reverse_x < min:
                return 0

        else:
            if reverse_x > max:
                return 0

        return reverse_x
