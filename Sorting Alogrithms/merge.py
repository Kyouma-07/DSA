class MergeSort:
    
    def __init__(self):
        pass
    
    def mergesort(self, arr: list[int], left : int, right : int): #we dont return anything cause we'll modify array in place.
        #we can return the whole list too 
        mid = (left+ right)//2

        if left >= right: #base case
            return
        
        self.mergesort(arr,left, mid) #recursive call to sort from left  to mid
        self.mergesort(arr,mid+1, right) # recursive call to sort from mid+1 to right
        self.merge(arr, left, mid , right) #call the merge function to merge the left and right subarrys

    
    def merge(self, arr: list[int], left, mid, right): #function to merge subarrays

        temp = [] #temporary array to store values
        i = left
        j = mid+1

        while ( i <= mid  and j <= right):  # check values from both subarrays and append smaller to temp array
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j  += 1

        #append the remianing values from left subarray to temp array if any...
        while ( i<= mid):
            temp.append(arr[i])
            i += 1
        
        #append the remaining values from right subbary to temp arry if any...
        while ( j <= right):
            temp.append(arr[j])
            j += 1

        #store the values back in original array
        for k in range(len(temp)):
            arr[left+k] = temp[k]

if __name__ =="__main__":
    arr = [ 35, 50 , 15 , 25 ,80, 20 , 90, 45]
    sorting = MergeSort()
    sorting.mergesort(arr, 0 , len(arr)-1)
    print("Sorted Array:" ,arr)


"""def mergesort(self, array , low , high):
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


"""