class CircularQueue:

    def __init__(self,capacity):
        self.capacity = capacity
        self.rear = -1
        self.front = -1
        self.queue = [0]* capacity

    
    def enqueue(self,value: int):

        if self.isfull():
            return "Queue is Full , cannot enqueue"
        
        if self.front == -1:  # condition when the inserting the 1st element
            self.front = 0
            self.rear = 0  # don't need to manually assign rear to 0 , but this's fine too
            self.queue[self.rear] = value
        
        else:
            self.rear = (self.rear+1)%self.capacity # wrapping around to implement circular behaviour
            self.queue[self.rear] = value
    
    def dequeue(self):

        if self.isempty():  # condition for when front queue is empty
            return "Underflow"
        
        if(self.front == self.rear): # condition when only 1 element exists in queue
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front+1)% self.capacity  # wrapping around
            return temp
    
    def isfull(self):
        return (self.rear +1) % self.capacity == self.front
            
    
    def isempty(self):
        return self.front == -1
    

    def peek(self):
        if self.isempty():
            return "queue is empty"
        return self.queue[self.front]
    
    def size(self):
        if self.isempty():
            return 0
        return (self.rear - self.front + self.capacity) % self.capacity + 1

if __name__ == "__main__":
    cq = CircularQueue(5)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    print(cq.dequeue())
    print(cq.isempty())
    print(cq.isfull())
    print(cq.peek())
