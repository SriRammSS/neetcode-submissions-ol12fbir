class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleet=set()

        for i in range(len(position)):
            need=(target-position[i])/speed[i]

            fleet.add(int(need))

            
        
        return len(fleet)
        