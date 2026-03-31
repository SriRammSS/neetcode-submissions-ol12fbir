class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        s1_freq_count = Counter(s1)
        s2_freq_count = {}

        need = len(s1_freq_count)
        have = 0
        window_length = len(s1)
        left = 0

        for right in range(len(s2)):
            char = s2[right]
            s2_freq_count[char] = s2_freq_count.get(char, 0) + 1

            # FIX: check membership before comparing
            if char in s1_freq_count and s2_freq_count[char] == s1_freq_count[char]:
                have += 1

            if right - left + 1 == window_length:

                if have == need:
                    return True

                if s2[left] in s1_freq_count:
                    if s2_freq_count[s2[left]] == s1_freq_count[s2[left]]:
                        have -= 1
                    s2_freq_count[s2[left]] -= 1
                left += 1

        return False