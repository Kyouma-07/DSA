class LC162:


    def __init__ (self):
        pass


    def findPeakElement(self, arr :list[int]) -> int:

        len_arr = len(arr)
        left_ptr = 0
        right_ptr = len_arr - 1

        while (left_ptr < right_ptr):

            mid = (left_ptr + right_ptr)//2

            #check for downhill
            if arr[mid] > arr[mid+1]:
                #peak lies to the left
                right_ptr = mid
            
            #if still uphill
            else:
                left_ptr = mid + 1
        
        return left_ptr