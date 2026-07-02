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
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(a)+int(b))
                
                if tokens[i]=="-":
                    a=stack.pop()
                    b=stack.pop()

                    stack.append(int(b)-int(a))

                if tokens[i]=="*":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(a)*int(b))
                    
                if tokens[i]=="/":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(b)//int(a))

        return stack.pop()
                




        