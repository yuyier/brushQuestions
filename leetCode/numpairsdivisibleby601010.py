from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        result_num = 0
        mode_count = [0] * 60
        for i in time:
            result_num += mode_count[(60 - i % 60) % 60]
            mode_count[i % 60] += 1
        return result_num
