class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total=0

        operators=["+","-","*","/"]

        stack=[]

        for i in range(len(tokens)):
            

            if tokens[i] not in operators:

                stack.append(tokens[i])
            
            else:
                
                if tokens[i]=="+":
                    total=0
                    while stack :
                        total=int(stack.pop())+total
                    stack.append(total)
                
                if tokens[i]=="-":
                    total=0
                    while stack:
                        total=int(stack.pop())-total
                    stack.append(total)
                
                if tokens[i]=="*":
                    total=1
                    while stack:
                        total=total*int(stack.pop())
                    stack.append(total)
                if tokens[i]=="/":
                    while stack:
                        total=total//int(stack.pop())
                    stack.append(total)
        
        return stack.pop()
                




        