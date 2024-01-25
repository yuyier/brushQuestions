# goProject
刷题

(1)list
1.1 列表赋值内存变化
切片赋值，nums列表的内存id没有变：nums[:] = nums[-k:] + nums[:-k]
直接赋值，nums的内存id发生变化：nums = nums[-k:] + nums[:-k]

1.2 列表倒序：list[::-1]

1.3 python中for循环输出list（index,value）的两种方法
方法一：for index,value in enumerate(list1)
方法二：for i in range(list1):print(i,list1(i))
