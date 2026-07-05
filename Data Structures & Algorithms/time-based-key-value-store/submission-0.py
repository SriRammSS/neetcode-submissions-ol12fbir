class TimeMap:

    def __init__(self):
        self.timemap={}
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        keys=(key,timestamp)

        self.timemap[keys]=value

        

        

        

    def get(self, key: str, timestamp: int) -> str:
        keys=(key,timestamp)
        if keys in self.timemap.keys():
            return self.timemap.get(keys)
        else:
            return self.timemap.get((key,timestamp-1))
        
