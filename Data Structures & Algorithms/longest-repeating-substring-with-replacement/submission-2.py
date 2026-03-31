class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length=0
        i=0
        d=dict()

        for j in range(len(s)):
            if s[j] not in d:
                d[s[j]]=1
            else:
                d[s[j]]=d[s[j]]+1
            window_size=j-i+1
            num_of_diff_char_in_window=window_size-max(d.values())

            if num_of_diff_char_in_window > k:
                d[s[i]]=d[s[i]]-1
                i=i+1
            max_length=max(max_length,j-i+1)
        return max_length

    
    
            
