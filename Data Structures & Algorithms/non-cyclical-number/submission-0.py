class Solution:
    def isHappy(self, n: int) -> bool:
        seen=[]
        total=0
        while total not in seen:
            for i in str(n):
                total=total+(int(i)**2)
            n=total

            if total in seen:
                return False
            elif total==1:
                return True
            else:
                seen.append(total)
            total=0