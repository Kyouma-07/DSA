class Sorting:
    def __init__(self):
        pass

    def quicksort(self, array, low, high):
        if low < high:
            point = self.pivot(array, low, high)  # Use self.pivot
            self.quicksort(array, low, point - 1)  # Use self.quicksort
            self.quicksort(array, point + 1, high)

    def pivot(self, array, low, high):
        element = array[low]
        i = low
        j = high

        while i < j:
            while i < high and array[i] <= element:
                i += 1
            while j > low and array[j] > element:
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]

        array[low], array[j] = array[j], array[low]
        return j

    
    def quicksort2(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quicksort2(left) + middle + self.quicksort2(right)
    
    
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    sorting = Sorting()
    sorting.quicksort(arr, 0, len(arr) - 1)
    print("Sorted Array:", arr)
