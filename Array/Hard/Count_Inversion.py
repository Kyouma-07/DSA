from bisect import bisect_right, insort

class MergeSort:
    
    def __init__(self):
        pass
    
    def mergesort(self, arr: list[int], left : int, right : int):
        mid = (left+ right)//2
        
        count = 0
        if left >= right: #base case
            return count
        
        count += self.mergesort(arr,left, mid) #recursive call to sort from left  to mid
        count += self.mergesort(arr,mid+1, right) # recursive call to sort from mid+1 to right
        count += self.merge(arr, left, mid , right) #call the merge function to merge the left and right subarrys

        return count
    
    def merge(self, arr: list[int], left, mid, right): #function to merge subarrays

        temp = [] #temporary array to store values
        i = left
        j = mid+1
        count= 0

        while ( i <= mid  and j <= right):  # check values from both subarrays and append smaller to temp array
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                count += (mid-i) +1
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

        return count
    
    def numberOfInversion(self, arr):
        return self.mergesort(arr, 0 , len(arr)-1)
    

    #using binary search and 
    def count_inversions(self,arr : list[int]):
        sorted_list = []
        count = 0
        
        for num in arr:
            pos = bisect_right(sorted_list, num)
            count += len(sorted_list) - pos
            insort(sorted_list, num)
            
        return count




if __name__ =="__main__":
    arr = [5 , 3, 2, 4, 1]
    sorting = MergeSort()
    count = sorting.numberOfInversion(arr)
    print("Inversion Count" ,count)
    
