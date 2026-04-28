class Queue:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.front = 0
        self.rear = -1  # can keep rear as 0 too , make necesaary changes to other conditions then
        self.queue = [0]*capacity

    
    def enqueue(self, value: int):
        if self.rear == self.capacity -1:
            return "Queue Overflow"
        else:
            self.rear += 1
            self.queue[self.rear] = value

    def dequeue(self):
        if self.isempty():
            return "Queue is Empty, Underflow!!!"
        else:
            value = self.queue[self.front]
            self.front += 1
            return value
    
    def peek(self):
        if self.isempty():
            return "Empty Queue"
        else:
            return self.queue[self.front]
        
    def size(self):
        return self.rear - self.front + 1

    def isempty(self):
        return self.front > self.rear
    

if __name__ == "__main__":

    print("FIXED SIZE QUEUE")
    stack1 = Queue(10)
    for i in range(10):
        n = int(input(("Enter the value you want to push to queue  ")))
        stack1.enqueue(n)           
    
    print(stack1.dequeue())
    print(stack1.peek())
    print(stack1.isempty())
    print(stack1.size())