class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            s = s + str(len(strs[i])) + "#" + strs[i]
        return s

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i<len(s):
            j=i
            while s[j]!= "#":
                j=j+1
            length = int(s[i:j])
            full_str = s[j+1:length+j+1]
            result.append(full_str)
            i = j + length + 1
        
        return result