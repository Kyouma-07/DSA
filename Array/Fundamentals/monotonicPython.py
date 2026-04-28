class MonotonicStack:

    def __init__(self):
        pass

    def increase(self, arr: list[int]):
        stack = []

        for i in arr:
            while(stack and stack[-1] > i):
                stack.pop()
            stack.append(i)
        
        return stack
    
    def decrease(self, arr: list[int]):
        stack = []

        for i in arr:
            while(stack and stack[-1] < i):
                stack.pop()
            stack.append(i)

        return stack

if __name__ == "__main__":
    stack1 = MonotonicStack()
    arr= [5,3,2,1,4]
    print(stack1.increase(arr))
    print(stack1.decrease(arr))