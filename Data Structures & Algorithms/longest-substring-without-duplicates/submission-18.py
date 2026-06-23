class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        track=set()
        j=0
        max_length=1

        if s in {""," "}:
            return 1



        for i in range(len(s)):
            if s[i] not in track:
                track.add(s[i])
            else:
                if s[i] in track:
                    track.remove(s[i])
                    j=i
                track.add(s[i])
            length=i-j+1
            max_length=max(max_length,length)
        
        return max_length
            




        