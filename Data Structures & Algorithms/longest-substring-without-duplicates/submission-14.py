class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lookup=set()

        i=0
        j=0

        max_length=1

        if len(s)==0:
            return 0

        while j<len(s):

            if s[j] not in lookup:
                lookup.add(s[j])
                length=j-i
                max_length=max(max_length,length+1)
                j=j+1
            else:
                while s[j] in lookup:
                    lookup.remove(s[i])
                    i=i+1
                lookup.add(s[j])

                j=j+1
        return max_length
            

                

            
          
            
       
            
        