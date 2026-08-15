# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #2-pointer approach

        #fake-dummy node
        dummy = ListNode(0,head)

        slow = dummy
        fast = dummy

        #moving the fast-pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        #move both nodes till one hits the end first
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        #delete the node:
        slow.next = slow.next.next

        #return the head - dummy.next contains the ref to new_head in case old gets deleted
        return dummy.next