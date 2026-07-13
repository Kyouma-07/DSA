class LC153:

    def __init__(self):
        pass


    def findMin(self, arr: list[int]) -> int:

        left = 0
        right = len(arr) -1
        min_val  = arr[0]

        while (left <= right):
            mid = (left+ right)//2

            #check if the left half is sorted
            if arr[left] <= arr[mid]:
                #update the min value
                min_val = min(arr[left], min_val)

                #discard the left portion
                left = mid + 1
            
            #check if the right portion is sorted
            else:
                if arr[mid] <= arr[right]:
                    #update the min
                    min_val = min(arr[mid],min_val)

                    #discard the right half
                    right = mid -1
        
        return  (min_val)