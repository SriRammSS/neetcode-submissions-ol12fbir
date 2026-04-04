class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
    def find_length(self,head):
        if head is None:
            return None
        else:
            length=0
            curr=head
            while curr is not None:
                length=length+1
                curr=curr.next
        return length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        else:
            curr=head
            index=0
            length=self.find_length(head)
            remove_index=length-n
            if remove_index==0:
                head=None
                return head


            while curr is not None and index!=remove_index:
                prev=curr
                curr=curr.next
                index=index+1
            prev.next=curr.next
        
        return head
            
                
                
            
                
        