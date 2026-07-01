class MinStack:

    def __init__(self):
        self.stack=[]

        

    def push(self, val: int) -> None:
        return self.stack.append(val)
        

    def pop(self) -> None:
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        minstack=[self.stack[0]]
        
        for i in range(1,len(self.stack)):
            if self.stack[i] < minstack[-1]:
                minstack.pop()
                minstack.append(self.stack[i])
        return minstack[0]
            
