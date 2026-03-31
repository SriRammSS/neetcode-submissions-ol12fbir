class Solution:
    def isPalindrome(self, s: str) -> bool:

        i=0
        j=len(s)-1
        s=s.lower()

        

        while i<j:

            while i<j and s[i].isalnum()==False:
                i=i+1
            
            while i<j and s[j].isalnum()==False:
                j=j-1
            
            if s[i]!=s[j]:
                return False
            else:
                i=i+1
                j=j-1
        return True