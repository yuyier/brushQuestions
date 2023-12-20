from typing import Optional

from list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        first_hand, second_hand = head, head.next
        while second_hand:
            if first_hand.val == second_hand.val:
                second_hand = second_hand.next
            else:
                first_hand.next = second_hand
                second_hand = second_hand.next
                first_hand = first_hand.next
        first_hand.next = second_hand
        return head
