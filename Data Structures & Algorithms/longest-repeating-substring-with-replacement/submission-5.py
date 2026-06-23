class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        track={}

        max_length=0

        j=0

        for i in range(len(s)):

            if s[i] in track.keys():
                track[s[i]]=track[s[i]]+1
            else:
                track[s[i]]=1

            if i-max(track.values())+1>k:
                track[s[j]]=track[s[j]]-1
                j=j+1
            
            max_length=max(max_length,i-j+1)
        
        return max_length

            

            




        