class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        return self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()
        else:
            return None

        


    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None
        

    def getMin(self) -> int:
        if self.stack:
            return min(self.stack)
        else:
            return None
        
        
        
