class LC1708:
    
    def __init__(self):
        pass

    #optimal
    def subarrayK(self, arr: list[int], target : int) -> int:

        freq ={ 0: -1}  # { current_sum : at what index we find this current_sum}
        current_sum = 0
        max_len = 0

        for i in range(len(arr)):

            current_sum += arr[i]
            need = current_sum - target

            if need in freq:
                max_len = max(max_len ,  i - freq[need])
            
            if current_sum not in freq:
                freq[current_sum] = i
            
        return max_len
    
    #Brute force
    def subSum(self, arr: list[int], target: int) -> int:
       max_length = 0

       for i in range (len(arr)):
          current_sum = 0
         
          for j in range(i , len(arr)):
             current_sum += arr[j]

             if current_sum == target:
                length = j -i + 1

                if length > max_length:
                   max_length = length
         
       return max_length
    
    #for only +ve elements in array  (using a sliding window)
    def subSumPositive(self, arr: list[int], target : int)-> int:
        left = 0
        max_len = 0
        current_sum = 0

        for i in range (len(arr)):
           current_sum += arr[i]

           while current_sum > target and left <= i :
              current_sum -= arr[left]
              left += 1

           if current_sum == target:
              max_len = max(max_len, i-left+1)
        
        return max_len
            

if __name__ == "__main__":
    print("Hello world!!")
    obj = LC1708()
    print(obj.subarrayK([1,2,3,-3,1,1,1,4,2,-3], 3))
