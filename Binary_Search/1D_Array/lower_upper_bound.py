class Bounds:

    def __init__(self):
        pass

    def lowerBound(self, arr :list[int] ,target : int) -> int:
        n = len(arr)
        left = 0
        right = n-1
        ans = n

        while (left <= right):
            mid = (left+right)//2

            if arr[mid] >= target:
                ans = mid
                right = mid -1
            else:
                left = mid +1
        
        return ans
    
    def upperBound(self, arr: list[int] , target : int ) -> int:

        n = len(arr)
        left = 0
        right = n-1
        ans = n

        while (left <= right):
            mid = (left+right)//2

            if arr[mid] > target:
                ans = mid
                right = mid -1
            else:
                left = mid +1
        
        return ans
    
    def arrFloor(self, arr: list[int] , target : int ) -> int:
        n = len(arr)
        left = 0 
        right = n-1
        ans = -1

        while (left <= right):
            mid = (left+right)//2

            if arr[mid] <= target:
                ans = arr[mid]
                left = mid +1
            else:
                right = mid -1
        
        return ans
    
    def arrCeil(self, arr: list[int] , target: int ) -> int:
        n= len(arr)
        left = 0
        right = n-1
        ans = -1

        while(left <= right):
            mid = (left +right)//2

            if arr[mid] >= target:
                ans = arr[mid]
                right = mid-1
            else:
                left = mid + 1

        return ans