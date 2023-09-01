from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        maximum_num = 1
        list_result = []
        if finalSum % 2 != 0:
            return list_result
        num = 2 * maximum_num
        while finalSum - num > num:
            finalSum -= num
            list_result.append(num)
            maximum_num += 1
            num = 2 * maximum_num

        list_result.append(finalSum)
        return list_result
