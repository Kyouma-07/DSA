class Selection:
    def __init__(self):
        pass
    
    def selectionSort(self, arr: list[int]) -> list[int]:

        for i in range(len(arr)):
            min_index = i
            print(f"\n--- Iteration {i} ---")
            print(f"Starting array: {arr}")

            for j in range(i + 1, len(arr)):
                print(f"Comparing arr[{min_index}]={arr[min_index]} with arr[{j}]={arr[j]}")

                if arr[min_index] > arr[j]:
                    min_index = j
                    print(f"➡️ New minimum found at index {j}: {arr[j]}")

            print(f"Minimum element at index {min_index}: {arr[min_index]}")

            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]
                print(f"Swapped → {arr}")
            else:
                print("No swap needed")

        return arr
        
                    
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    sorting = Selection()
    sorting.selectionSort(arr)
    print("Sorted Array:", arr)