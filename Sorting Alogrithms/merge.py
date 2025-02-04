class MergeSort:
    
    def __init__(self):
        pass
    
    def mergesort(self, array , low , high):
        if low >= high:
            return;
        mid = (low+high)//2
        
        self.mergesort(array, low , mid)     #merge sort the left subarray
        self.mergesort(array , mid+1 , high) #mergesort the right subarray
        self.merge(array , low , mid , high) #merge the elements by comparison
    
    def merge(self , array , low , mid , high):
        #arr1 [low...mid]
        #arr2 [mid+1... high]
        
        temp  = []
        left = low
        right = mid+1
        
        print(f"Merging subarrays:")
        print(f"Left subarray: {array[low:mid+1]}")
        print(f"Right subarray: {array[mid+1:high+1]}")
        
        print(f"comparing {array[left]} and {array[right]}")
        
        while(left <= mid  and right <=high):
            if array[left] <= array[right]:
                temp.append(array[left])
                left += 1
            else:
                temp.append(array[right])
                right += 1
            print(f"Current temp: {temp}")
            
        while left <= mid:
            print(f"Adding remaining from left: {array[left]}")
            temp.append(array[left])
            left += 1
    
        while right <= high:
            print(f"Adding remaining from right: {array[right]}")
            temp.append(array[right])
            right += 1
        
        #copy the array back into the original array.
        for i in range(len(temp)):
            array[low + i] = temp[i]
        
if __name__ =="__main__":
    arr = [ 35, 50 , 15 , 25 ,80, 20 , 90, 45]
    sorting = MergeSort()
    sorting.mergesort(arr, 0 , len(arr)-1)
    print("Sorted Array:" ,arr)