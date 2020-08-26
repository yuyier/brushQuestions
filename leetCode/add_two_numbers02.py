# coding=utf-8
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from list_node import ListNode


class AddTwoNumbers02(object):
    def add_two_numbers(self, l1, l2):
        list1 = l1
        list2 = l2
        list3 = ListNode(0)
        head = list3
        carry_bit = 0
        while list1 or list2:
            val1 = 0
            val2 = 0
            if list1:
                val1 = list1.val
                list1 = list1.next
            if list2:
                val2 = list2.val
                list2 = list2.next
            val_sum = (val1 + val2 + carry_bit)
            val = val_sum % 10
            list3.next = ListNode(val)
            list3 = list3.next
            carry_bit = 1
            if val_sum / 10 < 1:
                carry_bit = 0
        if carry_bit:
            list3.next = ListNode(carry_bit)

        return head.next
