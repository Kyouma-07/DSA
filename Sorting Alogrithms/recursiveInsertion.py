class RecursiveInsertion:
    def __init__(self):
        pass

    def RecursiveInsert(self, arr: list[int], n : int):
    
        if n <= 1:
            return 
        self.RecursiveInsert(arr, n-1) #recursive call to depth.
        #comparing and shifting
        key = arr[n-1]
        j = n-2

        while(j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key

if __name__ == "__main__":
    print("hello world")