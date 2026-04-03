class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False
        pointer1=head
        pointer2=head
        

        while pointer1 and pointer2 and pointer2.next is not None:
            pointer1=pointer1.next
            pointer2=pointer2.next.next

            if pointer1==pointer2 :
                return True
        return False

        