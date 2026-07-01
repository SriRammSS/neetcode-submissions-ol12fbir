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
                    while stack :
                        total=int(stack.pop())+total
                
                if tokens[i]=="-":
                    while stack:
                        total=total-int(stack.pop())
                
                if tokens[i]=="*":
                    while stack:
                        total=total*int(stack.pop())
                if tokens[i]=="/":
                    while stack:
                        total=total/int(stack.pop())
        
        return total
                




        