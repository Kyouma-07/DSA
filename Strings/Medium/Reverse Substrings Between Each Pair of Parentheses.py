class lc1190:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []

        for i in s:

            if i != ')':
                stack.append(i)
            else:
                temp = []

                while stack[-1] != "(":
                    temp.append(stack.pop())
                
                #remove (
                stack.pop()

                #put back:
                stack.extend(temp)

        
        return "".join(stack)