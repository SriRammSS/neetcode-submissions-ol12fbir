class Solution:
    def isPalindrome(self, s: str) -> bool:

        s="".join(char for char in s if char.isalnum())

        left=0

        right=len(s)-1

        while left < right:

            if str.lower(s[left])!=str.lower(s[right]):
                return False
            else:
                left=left+1
                right=right-1
        
        if right<=left:
            return True
        