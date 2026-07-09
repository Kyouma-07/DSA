class LC81:

    def __init__(self):
        pass

    def search(self, arr : list[int], target : int) -> bool:

        n= len(arr)
        left = 0
        right = n - 1

        while (left <= right):
            mid  =  (left+right)//2

            if arr[mid] == target:
                return  True
            
            #check if left mid and right values match , if yes , increment left , decrement right by 1
            if arr[left] == arr[mid] == arr[right]:
                left += 1
                right -= 1
                continue
            
            #check if the left half is sorted:
            if arr[left] <= arr[mid]:
                #check if the target exists:
                if arr[left] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            #check if the right half is sorted:
            else:
                if arr[mid] < target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid -1
        
        return False
            

            


