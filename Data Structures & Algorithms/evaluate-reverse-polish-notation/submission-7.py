from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['*', "+", "-", "/"]
        if len(tokens)==1:
            return int(tokens[-1])
     
        for i in tokens:
            if i not in operations:
                stack.append(i)
            else:
                if i == "+":
                    if stack:
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(int(b) + int(a))
                elif i == "-":
                    if stack:
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(int(b) - int(a))
                elif i == "*":
                    if stack:
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(int(b) * int(a))
                else:
                    if stack:
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(int(int(b) / int(a)))

        return stack[0]