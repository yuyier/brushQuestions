from typing import Optional

import add_two_link_number03
import add_two_number01
import eventsplit2178
import kmaxsum2600
import matrixsum2679
from list_node import Lists, ListNode
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
# from num_identical_pairs1512 import NumIdenticalPairs
# from shuffle1470 import Shuffle
# from reverse_feft_words_offer58 import ReverseLeftWords
# from sum_odd_length_subarrays5503 import SumOddLengthSubarrays
# from game_guess_LCP01 import Game
from num_jewels_in_stones771 import NumJewelsInStones


def create_list01():
    list1 = [0]
    list2 = [0]
    # list1 = [2, 4, 3]
    # list2 = [5, 6, 4]
    # list1 = [7, 2, 4, 3]
    # list2 = [5, 6, 4]
    # list1 = [3, 5, 1, 7, 9]
    # list2 = [1]
    # list1 = [5]
    # list2 = [5]
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

def print_link_list(l1: Optional[ListNode]):
    while l1:
        print(l1.val)
        l1=l1.next


if __name__ == '__main__':
    finalSum = 10
    print(eventsplit2178.Solution().maximumEvenSplit(finalSum))

    # numOnes = 3
    # numZeros = 2
    # numNegOnes = 2
    # k = 6
    # print(kmaxsum2600.Solution().kItemsWithMaximumSum(numOnes,numZeros,numNegOnes,k))
    # nums = [[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]
    # nums = [[1]]
    # nums =[[1, 8, 16, 15, 12, 9, 15, 11, 18, 6, 16, 4, 9, 4], [3, 19, 8, 17, 19, 4, 9, 3, 2, 10, 15, 17, 3, 11],
    #  [13, 10, 19, 20, 6, 17, 15, 14, 16, 8, 1, 17, 0, 2], [12, 20, 0, 19, 15, 10, 7, 10, 2, 6, 18, 7, 7, 4],
    #  [17, 14, 2, 2, 10, 16, 15, 3, 9, 17, 9, 3, 17, 10], [17, 6, 19, 17, 18, 9, 14, 2, 19, 12, 10, 18, 7, 9],
    #  [5, 6, 5, 1, 19, 8, 15, 2, 2, 4, 4, 1, 2, 17], [12, 16, 8, 16, 7, 6, 18, 13, 18, 8, 14, 15, 20, 11],
    #  [2, 10, 19, 3, 15, 18, 20, 10, 6, 7, 0, 8, 3, 7], [11, 5, 10, 13, 1, 3, 4, 7, 1, 18, 20, 17, 19, 2],
    #  [0, 3, 20, 6, 19, 18, 3, 12, 2, 11, 3, 1, 19, 0], [6, 5, 3, 15, 6, 1, 0, 17, 13, 19, 3, 8, 2, 7],
    #  [2, 20, 9, 11, 13, 5, 1, 16, 14, 1, 19, 3, 12, 6]]
    # print(matrixsum.MatrixSum().matrixSum(nums))
    # l1, l2 = create_list01()
    # print(print_link_list(add_two_link_number03.Solution().addTwoNumbers(l1,l2)))

    # nums = [2,7,11,15]
    # target = 9
    # nums =  [3,2,4]
    # target = 6
    # nums = [3, 3]
    # target = 6
    # print(add_two_number01.AddTwoNumbers01().twoSum(nums, target))
    # J = "aA"
    # S = "aAAbbbb"
    # J = "z"
    # S = "ZZ"
    # print(NumJewelsInStones().numJewelsInStones(J, S))
    # guess = [1, 2, 3]
    # answer = [1, 2, 3]
    # guess = [2, 2, 3]
    # answer = [3, 2, 1]
    # print(Game().game(guess, answer))
    # link_list1, link_list2 = create_list01()
    # list_nums = [1]
    # list_nums = [1, 2]
    # list_nums = [1, 2, 3]
    # list_nums = [1, 4, 2, 5, 3]
    # list_nums = [1, 4, 2, 5]
    # list_nums = [10, 11, 12]
    # list_nums=[]
    # list_nums = [6, 9, 14, 5, 3, 8, 7, 12, 13, 1]
    # print(SumOddLengthSubarrays().sumOddLengthSubarrays(list_nums))
    # s = "abcdefg"
    # k = 2
    # s = "lrloseumgh"
    # k = 6
    # print(ReverseLeftWords().reverseLeftWords(s, k))

    # list_nums = [1, 1, 2, 2, 3, 2, 2, 4]
    # list_nums = [1, 1, 1, 1]
    # list_nums = [1, 2, 3, 4]
    # list_nums = [1, 2, 3, 1, 1, 3]
    # list_nums = [1, 2]
    # print(Shuffle().shuffle(list_nums, 1))
# print(NumIdenticalPairs().numIdenticalPairs(list_nums))
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
