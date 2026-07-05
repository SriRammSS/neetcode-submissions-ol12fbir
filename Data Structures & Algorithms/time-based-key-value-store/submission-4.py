class TimeMap:

    def __init__(self):
        self.timemap={}
        self.timestamp_record=[]
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp_record.append(timestamp)
        keys=(key,timestamp)

        self.timemap[keys]=value

        
    def get(self, key: str, timestamp: int) -> str:
        keys=(key,timestamp)
        if keys in self.timemap.keys():
            return self.timemap.get(keys)
        else:
            if self.timestamp_record[-1]<=timestamp:
                return self.timemap.get((key,self.timestamp_record[-1]))
            else:
                return ""
            
        
