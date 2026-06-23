from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter=Counter(t)

        s_counter={}

        have=0
        need=len(t)

        j=0

        strng=""

        if s==t:
            return s

        for i in range(len(s)):
            if s[i] in s_counter:
                s_counter[s[i]]=s_counter[s[i]]+1
            else:
                s_counter[s[i]]=1
            
            if s_counter[s[i]]==t_counter[s[i]]:
                have=have+1
            
            while have == need:
                strng=s[j:i+1]

                if s[j] not in t_counter.keys():
                    j=j+1
                else:
                    s_counter[s[j]]=s_counter[s[j]]-1
                    if s_counter[s[j]]<t_counter[s[j]]:
                        have=have-1
                    j=j+1
                    
               
        return strng

            


            