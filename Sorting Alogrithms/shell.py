def shell_sort_verbose(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            print(f"\nProcessing index {i}, value {temp} , comparing to index {j-gap}, value  {arr[j-gap]}")
            print(f"Initial array: {arr}")
            
            while j >= gap and arr[j - gap] > temp:
                print(f"Shifting {arr[j - gap]} from index {j - gap} to index {j}")
                arr[j] = arr[j - gap]
                j -= gap
                print(f"i = {i} , j = {j}")
            
            arr[j] = temp
            print(f"After shifts: {arr}")
        
        gap //= 2
        print(f"Gap size: {gap}")
    
    return arr


# Example usage
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = shell_sort_verbose(test_arr)