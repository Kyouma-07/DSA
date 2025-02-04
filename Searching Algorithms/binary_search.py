class Binary:
    
    def __init__(Self):
        pass
    
    #normal binary search
    #time complexity = O(logn)
    #space complexiyt = O(1)
    def search(Self, array, target):
        
        low = 0
        high= len(array)-1
        
        while low <= high:
            mid = (low+high)//2
            
            if array[mid] == target:
                print(f"Traget found at index: {mid}")
                return mid
            
            elif target <= array[mid]:
                
                high = mid-1
            
            else:
                low = mid+1
        
        print(f"Element {target} not found in the array:")
        return -1
    
    #binary search using recursion.
    #time complexity = O(logn)
    #space complexity = O(logn) stack usage.
    def binary_recursion(self,array , left , right, target):
        
        if left > right :
            print("Element not found:")
            return -1
        
        mid = (left+right)//2
           
        if target == array[mid]:
            print(f"Target element found at index {mid}:")
            return mid
            
        elif target < array[mid]:
             return self.binary_recursion(array,left, mid-1, target)
            
        else:
             return self.binary_recursion(array,mid+1 ,right , target)
             
    def binary_search(self, array, target):
        
        array = sorted(array)
        return self.binary_recursion(array, 0 , len(array)-1 , target)
            
            
if __name__ == "__main__":
    
    array = [1 , 2, 3, 4 , 5 , 6, 7 , 8, 9 , 10]
    target = int(input("Enter the element to search:"))
    sorter = Binary()
    sorter.search(array , target)