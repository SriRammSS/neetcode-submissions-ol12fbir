class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        track=set()

        for i in range(len(position)):
            need=(target-position[i])/speed[i]

            track.add(int(need))

            
        
        return len(track)
        