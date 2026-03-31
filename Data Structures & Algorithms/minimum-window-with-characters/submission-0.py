from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_freq = Counter(t)
        window_freq = {}

        left = 0
        result = ""
        result_len = float("inf")

        for right in range(len(s)):
            if s[right] in t_freq:
                window_freq[s[right]] = window_freq.get(s[right], 0) + 1

            while all(window_freq.get(k, 0) >= t_freq[k] for k in t_freq):
                if right - left + 1 < result_len:
                    result_len = right - left + 1
                    result = s[left:right+1]

                if s[left] in t_freq:
                    window_freq[s[left]] -= 1
                    if window_freq[s[left]] == 0:
                        del window_freq[s[left]]
                left += 1

        return result