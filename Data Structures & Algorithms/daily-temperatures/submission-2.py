class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result=[0] * len(temperatures)

        stack=[len(temperatures)-1]




        for i in range(len(temperatures)-2,-1,-1):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                stack.pop()
            if stack:
                greatest=stack[-1]
            else:
                greatest=i
            day=greatest-i
            result[i]=day
            stack.append(i)
            
        return result
                
                

        