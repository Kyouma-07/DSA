class LC1539:

    def findKthPositive(self, arr: list[int], k: int) -> int:
        
         left = 1
         right =  max(arr) + k

         while ( left <= right ):
            mid = (left + right) // 2

            #number of elements <= mid
            present = __import__("bisect").bisect_right(arr, mid)

            #missing numbers
            missing = mid - present

            if missing >= k:
                right = mid - 1
            else:
                left = mid + 1
        
         return left

    
    def findKthPositive1(self, arr: list[int], k: int) -> int:
        
        for num in arr:
            if ( num <= k):
                k += 1
            else:
                break
        
        return k

    
    def findKthPositive3(self, arr: list[int], k: int) -> int:
        
         left = 0
         right =  len(arr) -1

         while ( left <= right ):
            mid = (left + right) // 2

            missing = arr[mid] - (mid + 1)  #calculate the missing elements till (mid) index

            #if mssing < k
            if missing < k :
                left = mid +1
            else:
                right = mid - 1
        
         return left + k