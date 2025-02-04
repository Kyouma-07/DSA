class Insertion:
    def __init__(self):
        pass

    def selectionsort(self, array):
        # Start traversing from the second element (index 1)
        for i in range(1, len(array)):
            # Current element to be inserted
            key = array[i]
            print(f"Key (current element to be sorted): {key}")
            
            # Index of the last element in the sorted portion of the array
            j = i - 1
            print(f"Starting j (last index in the sorted portion): {j}")
            
            # Shift elements in the sorted portion that are larger than 'key' one step to the right
            while j >= 0 and array[j] > key:
                print(f"array[j]: {array[j]} is greater than key: {key}")
                array[j + 1] = array[j]
                print(f"Moved array[{j}] to array[{j + 1}] -> {array}")
                j -= 1  # Move one step left
                print(f"Decrementing j: {j}")
            
            # Insert the key into its correct position
            array[j + 1] = key
            print(f"Inserted key at array[{j + 1}] -> {array}")
            print(f"Array after iteration {i}: {array}\n")
        
        return array

# Main section
if __name__ == "__main__":
    # Unsorted array
    array = [64, 34, 25, 12, 22, 11, 90]
    
    # Create an instance of the Insertion class
    sorter = Insertion()
    sorter.selectionsort(array)
    print(f"sorted array : {array}")
