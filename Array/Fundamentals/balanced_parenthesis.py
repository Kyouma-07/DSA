class Balance:
    def __init__(self):
        self.stack = []
        self.top = -1

    
    #implementation 1
    def check_balanced(self, value: str):
        opening = [ "(" , "{", "[" ]  #use tuple or just "{(["
        for i in value:
            if i in opening:
                self.top +=1
                self.stack[self.top] = i
                
            else:
                #check if stack is empty at beginning , if yes then return False
                if self.isempty():
                    return False

                #check for cases and if match decrement the top by 1
                if (self.stack[self.top] == "[" and i == "]") or \
                   (self.stack[self.top] == "(" and i == ")") or \
                   (self.stack[self.top] == "{" and i == "}"):
                    self.top -= 1
                
                #if not match , return False
                else:
                    return False
        
        #return the empty status, if yes empty at END, string balanced, if not , string not balanced
        return self.isempty()


    #implementation 2
    def checkingbalanced(self, value : str):
        mapping = {
                    "]" :"[",
                    "}" : "{",
                    ")" : "("   
        }

        for i in value:
            if i in mapping:
                if self.isempty():
                    return False
                if self.stack[self.top] != mapping[i]:
                    return False
                else:
                    self.top -= 1
            elif i in "([{":
                #if self.top == self.capacity -1   ## use this when the stack has limited space , capacity is defined
                self.top += 1
                self.stack[self.top] = i

        return self.isempty()
    
    def isempty(self):
        return self.top == -1


""" Balanced parentheses

Next Greater Element 🔥

Monotonic stack

Largest rectangle in histogram
"""