class Remove_Duplicate:

    def __init__ (self):
        pass

    def removeduplicates(self, arr: list[int])-> list[ list[int] | int]:
        n = len(arr)
        i = 0

        while(i < n):
            j = 0

            while( j < i):
                if arr[i] == arr[j]:
                    break # break the loop after the duplicate is found.
                j += 1  # increment the counter till duplicate is found.

            if (j < i): #if j < i  we run a loop from i to n-1 to shift the elements
                for k in range(i,n-1):
                    arr[k] = arr[k+1]
                n -= 1 # decrement n  cause the last value is just copy or garbage.   
                #[1,2,2,3,4,5,5] -> [1, 2 , 3, 4, 5, 5, 5] last 5 is garbage , we shift the elements to left.

            else:
                i += 1  # if nothing , we update the value to i
        return [arr[0:n], n]
        #Time complexity = 0(n^2), space = 0(1)
    
    def remove2(self, arr: list[int]):

        #using set, not in place, can work on unsorted arrays: time,space = O(n)
        unique = list(set(arr))  #
        for i in range(len(unique)):
                arr[i] = unique[i]
            
        return len(unique)
    

    #using hashmap, Time = 0(n) , space = O(n)
    def remove_duplicates_with_count(self, arr:list[int]):
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1
       
        i = 0
        for num in freq:
            arr[i] = num
            i += 1

        return i, freq 
    
    #using pointer pass, works only if the array is sorted.
    def remove3(self, arr: list[int]):

        i = 0 
        n= len(arr)
        for j in range(1, n):
            if arr[j] != arr[i]:
                i += 1
                arr[i] = arr[j]
        
        return[arr[0: i+1], i+1]

            
if __name__ == "__main__":
    obj = Remove_Duplicate()
    print(obj.remove3([1,2,2,3,4,5,5, 6, 6, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9 , 10 , 10]))