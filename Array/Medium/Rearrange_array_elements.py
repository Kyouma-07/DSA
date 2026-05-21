class LC2149:

    def __init__(self):
        pass


    def rearrangeArray(self, arr: list[int]) -> list[int]:
         n= len(arr)
         arr1 =[]
         arr2 = []

         for i in range (n):
             if arr[i] > 0:
                 arr1.append(arr[i])
             if arr[i] < 0:
                 arr2.append(arr[i])
        
        #since arr is even

         for i in range(n//2):
             arr[2*i] = arr1[i]
        
         for i in range (n//2):
             arr[(2*i) +1]= arr2[i]
        
         return arr
    
    def rearrangeArray1(self, arr: list[int]) -> list[int]:
        n = len(arr)
        new_arr = [0]*n
        pos_index = 0
        neg_index = 1

        for i in range(n):
            if arr[i] > 0:
                new_arr[pos_index] = arr[i]
                pos_index += 2
            else:
                new_arr[neg_index] = arr[i]
                neg_index += 2
        
        return new_arr
    
    #if arr contains unequal amount of +ve and -ves
    def rerrangeUnequal(self, arr: list[int]) -> list[int]:
        n = len(arr)
        pos =[]
        neg = []

        for i in range (n):
             if arr[i] > 0:
                 pos.append(arr[i])
             if arr[i] < 0:
                 neg.append(arr[i])
        
        i = j = 0
        result = []

        while i < len(pos) and j < len(neg):
            result.append(pos[i])
            result.append(neg[j])
            i += 1
            j += 1

        while i < len(pos):
            result.append(pos[i])
            i += 1
        
        while j < len(neg):
            result.append(neg[j])
            j += 1

        return result
    
    #modifying original arr instead.
    def rerrangeUnequal1(self, arr: list[int]) -> list[int]:
        n = len(arr)
        pos =[]
        neg = []

        for i in range (n):
             if arr[i] > 0:
                 pos.append(arr[i])
             elif arr[i] < 0:
                 neg.append(arr[i])
        
        i = j =k = 0

        while i < len(pos) and j < len(neg):
            arr[k] = pos[i]
            k += 1
            i += 1

            arr[k] = neg[j]
            k += 1
            j += 1
        
        while i < len(pos):
            arr[k] = pos[i]
            k += 1
            i += 1
        
        while j < len(neg):
            arr[k] = neg[j]
            k += 1
            j += 1
        
        return arr

if __name__ == "__main__":
    print("hello world")
    obj = LC2149()
    print(obj.rerrangeUnequal([3,1,-2,-5,2,-4,8, -8 , 9 , 10]))