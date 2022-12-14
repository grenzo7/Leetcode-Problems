# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if head == None:
        #     return False
        # slow = head
        # fast = head.next
        # while fast and fast.next:
        #     if slow == fast:
        #         return True
        #     slow = slow.next
        #     fast = fast.next.next
        # return False
        
        # curr = head
        # while curr:
        #     if curr.val == None:
        #         return True
        #     curr.val = None
        #     curr = curr.next
        # return False

        temp = set()
        curr = head
        while curr:
            if curr in temp:
                return True
            temp.add(curr)
            curr = curr.next
        return False
            