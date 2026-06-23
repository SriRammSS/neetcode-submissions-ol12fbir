class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        track=set()
        j=0
        max_length=1

        for i in range(len(s)):
            if s[i] not in track:
                track.add(s[i])
            else:
                while s[i] in track:
                    track.pop()
                    j=j+1
                track.add(s[i])
            length=i-j+1
            max_length=max(max_length,length)
        
        return max_length
            




        