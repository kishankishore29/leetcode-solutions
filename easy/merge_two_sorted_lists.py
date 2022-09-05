from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2

        if not list2:
            return list1

        runner_1, runner_2 = list1, list2

        if list1.val < list2.val:
            new_head = list1
            runner_1 = runner_1.next
        else:
            new_head = list2
            runner_2 = runner_2.next

        new_tail = new_head

        while runner_1 and runner_2:

            if runner_1.val < runner_2.val:
                new_tail.next = runner_1
                new_tail = runner_1
                runner_1 = runner_1.next
            else:
                new_tail.next = runner_2
                new_tail = runner_2
                runner_2 = runner_2.next

        if runner_1:
            new_tail.next = runner_1

        if runner_2:
            new_tail.next = runner_2

        return new_head
