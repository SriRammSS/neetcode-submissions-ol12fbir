class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]

        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minstack)==0 or self.minstack[-1] > self.stack[-1]:
            self.minstack.append(self.stack[-1])
        else:
            self.minstack.append(self.minstack[-1])

            
        
        

    def pop(self) -> None:
        if self.minstack[-1]==self.stack[-1]:
            self.minstack.pop()
        return self.stack.pop()


        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
            
