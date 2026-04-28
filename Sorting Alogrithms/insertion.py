class Insertion:
    def __init__(self):
        pass

    
    def insertion(self, arr: list[int]) -> list[int]:
        for i in range(1, len(arr)):
            key = arr[i] # element to be swapped
            j = i-1 # index of the last element in the sorted portion of the array.

            while( j>= 0 and arr[j] > key):
                arr[j+1] = arr[j]
                j -= 1
            
            arr[j+1] = key
        
        return arr


# Main section
if __name__ == "__main__":
    # Unsorted array
    array = [64, 34, 25, 12, 22, 11, 90]
    
    # Create an instance of the Insertion class
    sorter = Insertion()
    sorter.insertion(array)
    print(f"sorted array : {array}")
