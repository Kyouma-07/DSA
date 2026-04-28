class FixedStack:

    def __init__(self, capacity : int):
        self.stack =  []
        self.capacity = capacity

    
    def push(self, value: int):
        if len(self.stack) == self.capacity:
            return "Stack Overflow"
        self.stack.append(value)

    def pop(self):
        if self.isempty():
            return "stack underflow"
        else:
            return self.stack.pop()
        
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if self.isempty():
            return "Empty Stack"
        return self.stack[-1]

    def isempty(self):
        return len(self.stack) == 0
    

if __name__ == "__main__":
    print("FIXED SIZE STACK")
    stack1 = FixedStack(5)
    for i in range(5):
        n = int(input(("Enter the value you want to push to stack:  ")))
        stack1.push(n)           
    
    print(stack1.pop())
    print(stack1.peek())
    print(stack1.isempty())
    print(stack1.size())