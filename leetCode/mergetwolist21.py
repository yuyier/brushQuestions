# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from list_node import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_result = list_head = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                list_result, list1 = self.listResult(list_result, list1)
            else:
                list_result, list2 = self.listResult(list_result, list2)
        list_result.next = list1 if list1 else list2
        return list_head.next

    def listResult(self, list_result: Optional[ListNode], list_to_result: Optional[ListNode]) -> Optional[ListNode]:
        list_result.next = list_to_result
        list_to_result = list_to_result.next
        list_result = list_result.next
        return list_result, list_to_result
