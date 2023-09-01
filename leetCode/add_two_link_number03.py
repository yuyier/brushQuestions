"""
给你两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
你可以假设除了数字0之外，这两个数字都不会以零开头。

输入：l1 = [7, 2, 4, 3], l2 = [5, 6, 4]
输出：[7, 8, 0, 7]
示例2：

输入：l1 = [2, 4, 3], l2 = [5, 6, 4]
输出：[8, 0, 7]
示例3：

输入：l1 = [0], l2 = [0]
输出：[0]"""
from typing import Optional
from list_node import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_list = ListNode(0)
        list1_num = 0
        list2_num = 0
        while l1:
            list1_num = list1_num * 10 + l1.val
            l1 = l1.next
        while l2:
            list2_num = list2_num * 10 + l2.val
            l2 = l2.next
        sum_num = list1_num + list2_num

        while sum_num // 10 > 0:
            list_node = ListNode(sum_num % 10)
            list_node.next = result_list.next
            result_list.next = list_node
            sum_num = sum_num // 10

        result_list.val = sum_num % 10

        return result_list
