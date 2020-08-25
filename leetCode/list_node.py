class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Lists(object):
    def createList(self, lists):
        head = None
        for item in lists:
            if not head:
                head = ListNode(item)
                p = head
            else:
                p.next = ListNode(item)
                p = p.next
        return head
