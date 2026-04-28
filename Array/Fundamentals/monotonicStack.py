class Monotonic:

    def __init__(self , capacity: int):
        self.capacity = capacity
        self.stack = [0]* capacity
        self.top = -1
    

    def increasingStack(self, arr: list[int]):

        for i in range(len(arr)):
             while self.top != -1 and self.stack[self.top] > arr[i]:
                 self.top -=1
             
             self.top += 1
             self.stack[self.top] = arr[i]
        
        return self.stack[:self.top+1]
    

    def decreasingStack(self, arr: list[int]):

        for i in range(len(arr)):
             while self.top != -1 and self.stack[self.top] < arr[i]:
                 self.top -=1
             
             self.top += 1
             self.stack[self.top] = arr[i]
        
        return self.stack[:self.top+1]


if __name__ == "__main__":
    print("Hellow world")
    length = int(input("Enter the maximum length of the arr:    "))
    total_elements = int(input("Enter the no. of elements you want to insert in the arr:    "))
    arr = [0]*total_elements
    for i in range(0,total_elements):
         temp = int(input("Enter the number you want to add:    "))
         arr[i] = temp

    stack1 = Monotonic(5)
    print(stack1.increasingStack(arr))
    print(stack1.decreasingStack(arr))