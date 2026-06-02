class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b="".join(str(n) for n in digits)
        b=int(b)+1
        c=[int(i) for i in str(b)]
        return c

        