class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet=1
        stack=[]
        for i in range(len(position)):
            while stack and position[i] > position[stack[-1]]:
                greatest_time=(target-position[i])/speed[i]
                smallest_time=(target-position[stack[-1]])/speed[stack[-1]]
                if greatest_time<smallest_time:
                    fleet=fleet+1
                stack.pop()
            stack.append(i)
        return fleet


            

        

           
            
                




            

            
        
        return len(fleet)
        