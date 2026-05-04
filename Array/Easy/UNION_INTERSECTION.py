class Union_Intersection:

    def __init__ (self):
        pass


    def union1(self, arr1 : list[int], arr2 : list[int]):
         s= set()

         for i in arr1:
             s.add(i)
        
         for i in arr2:
             s.add(i)
            
         return sorted(s)

    def union2(self, arr1: list[int], arr2: list[int]):

        i, j = 0, 0
        result = []

        #only happens if the array are sorted
        while i < len(arr1) and  j < len(arr2):
            if arr1[i] <= arr2[j]:
                if not result or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
            else:
                if not result or result[-1] != arr2[j]:
                    result.append(arr2[j])
                j += 1

        #remaining elements from arr1
        while i <  len(arr1):
            if not result  or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        
        #remaining elements from arr2
        while j < len(arr2):
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
        
        return result


    def intersection1(self, arr1: list[int], arr2: list[int]):
        set1 = set(arr1)
        result = set()

        for i in arr2:
            if i in set1:
                result.add(i)
        
        return list(result)
    
    def intersection2(self, arr1: list[int], arr2: list[int]):
        i , j = 0 , 0
        result = []

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                 if not result  or result[-1] != arr1[i]:
                     result.append(arr1[i])
                    
                 i += 1
                 j += 1
            
            return result