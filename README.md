# goProject
刷题

(1)list
切片赋值，nums列表的内存id没有变：nums[:] = nums[-k:] + nums[:-k]
直接赋值，nums的内存id发生变化：nums = nums[-k:] + nums[:-k]