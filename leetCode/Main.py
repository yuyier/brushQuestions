from list_node import Lists
# from add_two_numbers02 import AddTwoNumbers02
# from length_of_longest_substring03 import Solution
from find_median_sorted_array04 import FindMedianSortedArrays


def create_list():
    # list1 = [3, 5, 1, 7, 9]
    # list2 = [4, 6, 2, 1]
    list1 = [5]
    list2 = [5]
    link_list1 = (Lists().createList(list1))
    link_list2 = (Lists().createList(list2))
    return link_list1, link_list2


def index_str():
    str = 'absdfew'
    # print(str.index('e'))
    for index in range(len(str)):
        print(str[index])


def return_str():
    str = "asbsdssdfuuuuiyyyytfvvvhjyiomnb"
    return str


def return_lsit():
    # list1 = [1, 3, 4, 5, 6, 7, 8, 9, 10]
    # list2 = [2]
    # 5.5
    # list1 = [2]
    # list2 = [1, 4]
    # 2
    # list2 = [5]
    # list1 = [3, 4]
    # 4
    # list1 = [1]
    # list2 = [3, 5]
    # 3
    # list2 = [1, 3, 4, 5, 6, 7, 8, 9, 10]
    # list1 = [2]
    # list1 = [1, 3, 4]
    # list2 = [2]
    # list2 = [1, 3, 4]
    # list1 = [2, 6]
    # 3
    # list2 = [1, 4, 6]
    # list1 = [2, 3, 9, 10]
    # 4
    # list2 = [1, 4, 6, 20]
    # list1 = [2, 3, 9, 10, 18]
    # 6
    list2 = [1, 2]
    list1 = [3, 4]
    return list1, list2


if __name__ == '__main__':
    # l1, l2 = create_list()
    # list = AddTwoNumbers02().add_two_numbers(l1, l2)
    # print(list)
    # index_str()
    # print(Solution().lengthOfLongestSubstring(return_str()))
    list1, list2 = return_lsit()
    print(FindMedianSortedArrays().findMedianSortedArrays(list1, list2))
