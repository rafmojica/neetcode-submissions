# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get to middle of list
        # reverse second half of the list
        fast = head
        slow = head

        # get to middle of the list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # [1, 2, 3, 4, 5]
        # slow.next --> [4, 5]

        # [1, 2, 3, 4]
        # slow --> [3, 4]

        second = slow.next
        prev = None
        slow.next = None

        while second:
            oldNext = second.next
            second.next = prev
            prev = second
            second = oldNext

        # [1, 2, 3, 4, 5]
        # head --> [1, 2, 3]
        # prev --> [5, 4]
        # --> [1, 5, 2, 4, 3]

        first, second = head, prev
        while second:
            oldFirstNext, oldSecondNext = first.next, second.next
            first.next, second.next = second, oldFirstNext
            first, second = oldFirstNext, oldSecondNext
