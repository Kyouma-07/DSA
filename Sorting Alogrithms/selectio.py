class Selection:
    def __init__(self):
        pass
    
    def SelectionSort(self, array):
        for i in range(len(array)):
            min = i #selecting the first index as the minimum element
            
            for j in range(i+1, len(array)):
                if array[j] < array[min]: #check if the element at j < min element
                    min = j
            array[i],array[min] = array[min],array[i]
            
        return array
    
    
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    sorting = Selection()
    sorting.SelectionSort(arr)
    print("Sorted Array:", arr)