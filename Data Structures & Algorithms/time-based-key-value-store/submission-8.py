from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store=defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp,value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store.keys():
            return ""
        
        low=0
        high=len(self.store[key])-1
        record=self.store[key]
        val=""

        while low<=high:
            mid=(low+high)//2

            if record[mid][0] <= timestamp:
                low=mid+1
                val=record[mid][1]
            else:
                high=mid-1
        
        return val
            


   
        
