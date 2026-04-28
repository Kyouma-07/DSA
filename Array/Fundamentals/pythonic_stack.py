class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self, value: int):
        self.stack.append(value)
    
    def pop(self):
        if self.isempty():
            return "stack underflow"
        self.stack.pop()
    
    def isempty(self):
        return len(self.stack) == 0
          
    
    def peek(self):
        if self.isempty():
            return "stack is empty"
        else:
            return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    #this is a pythonic way to implement stack with list

if __name__ == "__main__":
    print("FIXED SIZE STACK")
    stack1 = Stack()
    for i in range(5):
        n = int(input(("Enter the value you want to push to stack:  ")))
        stack1.push(n)           
    
    print(stack1.pop())
    print(stack1.peek())
    print(stack1.isempty())
    print(stack1.size())
