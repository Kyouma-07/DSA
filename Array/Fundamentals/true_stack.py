class TrueStack:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = [0] * capacity   #[0, 0, 0, 0, 0] , preallocating memeory
        self.top = -1

    
    def push(self, value: int):
         if self.top == self.capacity-1:
             return " Stack overflow!!!"
         else:
             self.top += 1
             self.stack[self.top] = value
             
    
    def isempty(self):
        return self.top == -1
    
    def pop(self):
        if self.isempty():
            return " Stack underflow !!!"
        else:
            temp = self.stack[self.top]
            self.top -= 1
            return temp
    
    def peek(self):
        if self.isempty():
            return " stack is empty"
        else:
            return self.stack[self.top]
        
    def size(self):
        return self.top+1

if __name__ == "__main__":
    print("FIXED SIZE STACK")
    stack1 = TrueStack(10)
    for i in range(10):
        n = int(input(("Enter the value you want to push to stack:  ")))
        stack1.push(n)           
    
    print(stack1.pop())
    print(stack1.peek())
    print(stack1.isempty())
    print(stack1.size())