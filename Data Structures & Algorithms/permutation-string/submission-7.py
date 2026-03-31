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

                left_char = s2[left]

                if left_char in s1_freq_count:
                    if s2_freq_count[left_char] == s1_freq_count[left_char]:
                        have -= 1

                    s2_freq_count[left_char] -= 1
                left += 1

        return False