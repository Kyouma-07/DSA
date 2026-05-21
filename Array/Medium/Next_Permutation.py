class LC57:

    def __init__(self):
        pass


    def nextPermutation(self, arr: list[int]) -> None:

        breaking_point = -1
        n = len(arr)

        for i in range( n-2, -1 , -1):
           if arr[i] < arr[i+1]:
                breaking_point = i
                break
        
        if breaking_point == -1:
                arr.reverse()
                return
        
        for i in range ( n-1, breaking_point, -1):
             if arr[i] > arr[breaking_point]:
                  arr[i], arr[breaking_point] = arr[breaking_point], arr[i]
                  break
        
        arr[breaking_point+1:] = reversed(arr[breaking_point+1:])
    
        #can create a reverse function and reverse from one index to other.
