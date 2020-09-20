from list_node import Lists
from tree_node import CreateTree

# from add_two_numbers02 import AddTwoNumbers02
# from length_of_longest_substring03 import Solution
# from find_median_sorted_array04 import FindMedianSortedArrays
# from longest_palindrome05 import LongestPalindrome
# from convert06 import Convert
# from Reverse07 import Reverse
# from sum_of_left_leaves404 import SumOfLeftLeaves
# from running_sum1480 import RunningSum
# from kids_with_candies1431 import KidsWithCandies
from num_identical_pairs import NumIdenticalPairs


def create_list01():
    # list1 = [3, 5, 1, 7, 9]
    # list2 = [4, 6, 2, 1]
    list1 = [5]
    list2 = [5]
    link_list1 = (Lists().createList(list1))
    link_list2 = (Lists().createList(list2))
    return link_list1, link_list2


def index_str02():
    str = 'absdfew'
    # print(str.index('e'))
    for index in range(len(str)):
        print(str[index])


def return_str03():
    str = "asbsdssdfuuuuiyyyytfvvvhjyiomnb"
    return str


def return_lsit04():
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


def palindromeStr05():
    # s = 'aba'
    # s = 'aatuibbb'
    # s = 'aa'
    # s = 'aaa'
    # s = 'aaaaaaaabaaaaaaac'
    # s = 'qwerttyyyu'
    # s = 'aba'
    s = 'babad'
    return s


def convertStr06():
    # str = 'LEETCODEISHIRING'
    # str='LEETCODEISHIRING'
    # str='PAYPALISHIRING'
    # str='PAYPALISHIRIN'
    # str='PAYPALISHIRI'
    # str='PAYPALISHIR'
    # str=''
    # str = 'PAY'
    # str = 'PAYP'
    # str="A"
    str = "AB"
    return str


def reverseNum():
    # num = 123
    # num = -123
    # num = -9463847412
    # num = -8463847412
    # num = 8463847412
    # num = 7463847412
    # num = -20
    num = 20
    return num


if __name__ == '__main__':
    # list_nums = [1, 1, 2, 2, 3, 2, 2, 4]
    # list_nums = [1, 1, 1, 1]
    # list_nums = [1, 2, 3]
    list_nums = [1, 2, 3, 1, 1, 3]
    print(NumIdenticalPairs().numIdenticalPairs(list_nums))
# list = [1, 2, 3, 4, 5]
# list = [1, 2, 3]
# list = [1, 2, 3, 4, 5, 6, 7]
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list = []
# list = [1]
# list = [1, 2]
# extra = 2
# print(KidsWithCandies().kidsWithCandies(list, extra))
# print(RunningSum().runningSum(list))
# tree = CreateTree().return_tree(list)
# print(SumOfLeftLeaves().sumOfLeftLeaves(tree))
# reverse_num = reverseNum()
# print(Reverse().reverse(reverse_num))
# print(pow(2, 31))
# str = convertStr()
# print(Convert().convert(str, 1))
# print(Convert().convert(str, 3)=='LCIRETOESIIGEDHN')
# print(Convert().convert(str, 4)=='LDREOEIIECIHNTSG')
# assert Convert().convert(str, 3), "LCIRETOESIIGEDHN"

# s = palindromeStr()
# print(s[0] == s[2])

# print(LongestPalindrome().longest_palindrome(s))

# l1, l2 = create_list()
# list = AddTwoNumbers02().add_two_numbers(l1, l2)
# print(list)
# index_str()
# print(Solution().lengthOfLongestSubstring(return_str()))
# list1, list2 = return_lsit()
# print(FindMedianSortedArrays().findMedianSortedArrays(list1, list2)
