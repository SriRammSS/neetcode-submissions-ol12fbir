class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            while s[right] in track:
                track.remove(s[left])
                left = left + 1
            track.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len
        

  
        