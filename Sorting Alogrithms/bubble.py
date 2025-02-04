class Bubble:
    
    def __init__ (Self):
        pass
    
    def bubblesort(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr
    
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    sorting = Bubble()
    sorting.bubblesort(arr)
    print("Sorted Array:", arr)