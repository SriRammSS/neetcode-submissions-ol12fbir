class Solution:

    def encode(self, strs: List[str]) -> str:

        encod=[]

        for i in strs:
            encod.append(str(len(i))+'#'+i)
        s="".join(encod)

        return s

    def decode(self, s: str) -> List[str]:

        i=0

        decod=[]

        while i < len(s):
            j=i

            while s[j]!='#':
                j=j+1
            
            leng=int(s[i:j])

            decod.append(s[j+1:leng+(j+1)])

            i=j+1+leng
        return decod


        




       

