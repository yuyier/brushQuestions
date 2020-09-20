# coding=utf-8

class KidsWithCandies(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        list_bool = []
        for candy in candies:
            if (candy + extraCandies) >= max_candies:
                list_bool.append(True)
            else:
                list_bool.append(False)

        return list_bool
