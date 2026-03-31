class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded=[]
        
        for i in range(len(strs)):
            encoded.append(str(len(strs[i]))+"#"+strs[i])
        
        s="".join(encoded)

        return s

    def decode(self, s: str) -> List[str]:

        decoded=[]
        i=0

        while i<len(s):
            j=i
        

            while s[j]!="#":
                j=j+1
            length=int(s[i:j])

            decoded.append(s[j+1:length+(j+1)])

            i=j+1+length
        
        return decoded
            


