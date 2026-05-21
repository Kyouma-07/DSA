class LC128:

    def __init__ (self):
        pass


    def longestConsecutiveBrute(self, arr: list[int]) -> int:
        
        if len(arr) == 0:
            return 0

        longest = 1

        for i in range(len(arr)):
             x = arr[i]
             count = 1

             while (self.linear_search(arr, x+1) == True):
                 x += 1
                 count += 1
            
             if count > longest:
                 longest = count
        
        return longest


    
    def linear_search(self , arr : list[int], target : int):
        
        for i in range(len(arr)):
            if arr[i] == target:
                return True
                
        return False
    

    def longestConsecutiveBetter(self, arr : list[int]) -> int:

        if len(arr) == 0:
            return 0
        
        arr.sort()
        longest = 1

        for i in range(len(arr)):
            count = 1

            for j in range(i+1 , len(arr)):
                if arr[j] == arr[j-1]:
                    continue
                elif  arr[j] == arr[j-1]+1:
                    count += 1
                else:
                    break
            
            longest = max(longest, count)

        return longest
    
    def longestConsecutive(self, arr: list[int]) -> int:

        if len(arr) == 0:
            return 0
         
        longest = 1
        set_arr = set(arr)

        for num in set_arr:
            if num-1 not in set_arr:
                current = num
                count = 1

                while  current+1  in set_arr:
                    current += 1
                    count += 1
            
                longest = max(longest, count)
        return longest