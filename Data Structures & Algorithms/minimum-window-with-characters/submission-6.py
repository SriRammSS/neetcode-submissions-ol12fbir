from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_freq = Counter(t)
        window_freq = {}

        have = 0
        need = len(t_freq)

        left = 0
        result = ""
        result_len = float("inf")

        for right in range(len(s)):
            if s[right] in t_freq:
                window_freq[s[right]] = window_freq.get(s[right], 0) + 1

                if window_freq[s[right]] == t_freq[s[right]]:
                    have =have + 1

            while have == need:
                if right - left + 1 < result_len:
                    result_len = right - left + 1
                    result = s[left:right+1]
                if s[left] in t_freq:
                    window_freq[s[left]]=window_freq[s[left]]-1
                    if window_freq[s[left]] < t_freq[s[left]]:
                        have=have-1
                left=left+1

                

        return result