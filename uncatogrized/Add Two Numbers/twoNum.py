class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''
        
        curr = l1.val
        while curr is not None:
            num1 = num1 + str(curr)
            curr = curr.next
        
        curr = l2.val
        while curr is not None:
            num2 = num2 + str(curr)
            curr = curr.next
        

        sum = int(num1) + int(num2)
        

