class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1

        while i<=j:
            if not s[i].lower().isalpha():
                i=i+1
            if not s[j].lower().isalpha():
                j=j-1

            if s[i].lower()!=s[j].lower():
                return False
                
            else:
                i=i+1
                j=j-1
        return True 



        