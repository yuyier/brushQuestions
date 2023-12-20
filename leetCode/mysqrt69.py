class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        last_max, last_min = x // 2, 0
        while last_max * last_max > x:
            last_max = last_max // 2
        last_min = last_max
        last_max = last_max * 2
        while last_min <= last_max:
            if last_min * last_min > x:
                break
            last_min = last_min + 1
        return last_min - 1
