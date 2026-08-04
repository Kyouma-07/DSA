class Solution:
    def findErrorNums(self, arr: list[int]) -> list[int]:
        n = len(arr)

        #using cyclic method
        for i in range(n):
             while 0 < arr[i] <= n and arr[i] != arr[arr[i] - 1]:
                crr_idx = arr[i] - 1
                #swap
                arr[crr_idx], arr[i] = arr[i], arr[crr_idx]
        
        for i in range(n):
            if arr[i] != i +1:
             return [arr[i] , i+1]
        
        return [-1, -1]
  