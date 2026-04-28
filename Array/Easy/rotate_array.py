class  Rotate:

    def __init__ (self):
        pass


    def rotate1(self, arr: list[int]) -> list[int]:
        if not arr:
         return arr

        n = len(arr)
        temp = arr[0]

        for i in range(1, n):
            arr[i-1] = arr[i]

        arr[n-1] = temp

        return arr

    def reverse(self, arr : list [int], left : int, right : int):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
    

    #optimal approach
    def rotate_left_k(self, k: int, arr: list[int]) -> list[int]:
        if not arr:
            return arr
        
        n= len(arr)
        k = k%n
        
        self.reverse(arr,0,n-1)  
        self.reverse(arr,0,n-k-1)   
        self.reverse(arr,n-k,n-1)  

        return arr
    
    def rotate_right_k(self, k:int, arr : list[int]) -> list[int]:
        if not arr:
            return arr
        
        n= len(arr)
        k = k%n
   
        self.reverse(arr,0,n-1)
        self.reverse(arr,0,k-1)
        self.reverse(arr,k,n-1)

        return arr

    #time = 0(n), space = 0(1)

    def left(self, k : int, arr: list[int]) -> list[int]:
        if not arr:
            return arr
        
        n= len(arr)
        k = k%n
        temp = [0]*n

        for i in range(len(arr)):
            temp[i] = (arr[(i+k)%n])
            #temp[(i - k) % n] = arr[i] this will also work
            #temp[(i + k) % n] = arr[i] for right rotation
        return temp

     
 
if __name__ == "__main__":
    obj = Rotate()
    print(obj.rotate_left_k(2,[1,2,3,4,5]))
    print(obj.rotate_right_k(2,[1,2,3,4,5]))
