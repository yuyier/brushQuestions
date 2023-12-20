from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list2 = digits[::-1]
        add_num = 0
        for index, num in enumerate(list2):
            if num == 9:
                list2[index] = 0
                add_num = 1
            else:
                list2[index] = num + 1
                add_num = 0
                break
        if add_num > 0:
            list2.append(1)
        return list2[::-1]
