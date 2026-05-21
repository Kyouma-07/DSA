class LC75:

    def __init__(self):
        pass


    def sortColorBrute(self, arr: list[int]):
        arr.sort()  #inplace sorting , time =  O(nlogn)
    
    def sortColorBetter(self, arr: list[int]):
        
        freq ={}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        index = 0
        for key in [0, 1, 2]:
            for i in range(freq.get(key,0)):
                arr[index] = key  
                index += 1
    
    def sortColorOptimal(self, arr: list[int]):

        mid = 0
        low = 0
        high = len(arr)-1

        while(mid <= high):  # we only sort the unsorted region, when mid > high => whole array is sorted.
            if arr[mid] == 0:
                arr[low], arr[mid] =arr[mid], arr[low]
                low += 1
                mid += 1

            elif arr[mid] == 1:
                mid += 1
            
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
            