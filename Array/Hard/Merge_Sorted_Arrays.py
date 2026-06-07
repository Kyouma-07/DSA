class LC88:

    def __init__(self):
        pass


    def merge(self, arr1: list[int], m : int , arr2: list[int], n : int):
        
        for i in range(n):
            arr1[m+i] = arr2[i]
        
        arr1.sort()

    
    def merge2(self, arr1: list[int], m : int , arr2: list[int], n : int):
         
         i = m-1
         j = n-1
         k = m+n-1

         while( i >= 0 and j >= 0):
             if arr1[i] > arr2[j]:
                 arr1[k] = arr1[i]
                 i -= 1
             else:
                 arr1[k] = arr2[j]
                 j -= 1

             k -= 1
         
         while j >= 0:
             arr1[k] = arr2[j]
             j -= 1
             k -= 1