class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False
        pointer1=head
        pointer2=head.next
        

        while pointer1 and pointer2 is not None:
            if pointer2.val<=pointer1.val:
                return True
            else:
                pointer1=pointer1.next
                pointer2=pointer2.next
        return False

        