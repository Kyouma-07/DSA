class Hashing_Basic:

    def __init__(self):
     pass


    #count frequency, brute force
    def freq(self, arr: list[int], number: int) -> int:
        count = 0
        for i in range(0, len(arr)):
            if arr[i] == number:
                count += 1
        return count
    
    #Time complexity = 0(n)
    #space = 0(1)
          
    #count freq using basic hashing: (fina all elements and their freq)
    def freq_hash(self, arr: list[int])-> dict[int,int]:
       frequency ={}
       for i in arr:
          if i in frequency:
             frequency[i] += 1
          else:
             frequency[i] = 1
       return frequency
    #using in built hashing use ( frequency = counter(arr))

    #count freq of given elements only
    def freq_counter_hash(self, arr: list[int], query: list[int]) -> list[int]:
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
       
        #result array containing the freq of given elements
        result = []
        for q in query:
           if q in freq:
              result.append(freq[q]) #always append values to empty list
           else:
              result.append(0)     
        return result
    

    #character hashing
    def freq_character(self, string: str) -> dict[str, int]:
       freq ={}  # strings are iterable in python , so no need to use unicode or ASCII
       for i in string:
          if i in freq:
            freq[i] += 1
          else:
               freq[i] = 1
       return freq
    

    #highest occuring element in an array
    def highest_freq(self, arr: list[int]) -> int:
       max_counter = 0
       max_element = arr[0]
       freq = {} 

       for i in arr:
          if i in freq:
             freq[i] += 1

          else:
             freq[i] = 1   

          #checking the freq with max_counter
          if freq[i] > max_counter:
             max_counter = freq[i]
             max_element = i

       return max_element       

   
    #character hashing and finding freq by queries
    def freq_character_hash(self, string: str, query: list[str]) -> list[int]:
        freq = {}
        for i in string:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
       
        #result array containing the freq of given elements
        result = []
        for q in query:
           if q in freq:
              result.append(freq[q]) #always append values to empty list
           else:
              result.append(0)     
        return result
    

    #first non repeating element in the array
    def non_repeating_hash(self, arr: list[int])-> int:
       freq ={}
       for i in arr:
          if i in freq:
               freq[i] += 1
          else:
               freq[i] = 1
         
       for i in arr:
          if freq[i] == 1:
             return i
         
       return -1
    #time = 0(n)
    #sapce = 0(n)


    #twosum using two pointers
    def twoSum(self,arr: list[int], target: int) -> list[int]:
       hashmap ={}

       for i in range(len(arr)):
          need = target - arr[i]
          if need in hashmap:
             return [hashmap[need] ,i]
          hashmap[arr[i]] = i
      
       return [-1, -1]  #no solution
    #Time = 0(n)
    #Space = 0(n)


    #longest subarray with sum K
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
    #dont break the inner iteration once the sum reaches above the target value cause the array may contain negative values.
    #Subarry sum equals K
    #Brute force:
    def counterSubarr(self, arr: list, target: int) -> int:
        counter = 0
        for i in range( len(arr)):
           current_sum = 0

           for j in range ( i , len(arr)):
              current_sum += arr[j]

              if current_sum == target:
                 counter += 1
         
        return counter
                
         

if __name__ == "__main__":
   print("Hello world")
   obj = Hashing_Basic()
   print(obj.counterSubarr([1,2,1,2,1],3))


"""Find most frequent element
Find first non-repeating element
Count frequency of characters in a string


🔥 Which method to pick in interviews instantly
🧩 Problems where Counter fails
⚔️ Real interview question walkthrough using hashing


"""