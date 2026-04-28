class RecrusiveBubble:

    def __init__(self):
        pass

    
    def RecursiveSort(self, arr: list[int], n : int):
        if n <= 1:
            return arr
        
        for i in range(0 , n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        
        self.RecursiveSort(arr,n-1)


if __name__ == "__main__":
    print("hello world!!")
    arr = [10, 7, 8, 9, 1, 5]
    sorting = RecrusiveBubble()
    sorting.RecursiveSort(arr,len(arr))
    print("Sorted Array:", arr)