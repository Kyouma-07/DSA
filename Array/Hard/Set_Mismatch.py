class LC645:
    
    def __init(self):
        pass

    def findErrorNumsBrute(self, arr: list[int]) -> list[int]:
        
        miss = -1
        repeat = -1

        for i in range(1,len(arr)+1):
            count = 0

            for j in range (0, len(arr)):
                if i == arr[j]:
                    count += 1
            
            if count == 2:
                repeat = i
            
            elif count == 0:
                miss = i
        
        return [repeat,miss]
    #time = O(n^2)
    #space =  O(1)

    def findErrorNumsMap(self, arr: list[int]) -> list[int]:
        
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        repeat = -1
        miss = -1

        for i in range(1, len(arr) + 1):
            if freq.get(i, 0) == 2:
                repeat = i
            elif i not in freq:
                miss = i

        return [repeat, miss]
    #time = o(n), space = O(n)

    def findErrorNumsMath(self, arr: list[int]) -> list[int]:
        n = len(arr)
        #S-Sn   (sum of give arr) -  (sum of first n natual no)  x-y
        #Ssq - Snsq  (sum of sq of array element) - (sum of sq of first n no.) x^2-y^2

        sum_natural = n*(n+1)//2
        sumsq_natural = n*(n+1)*(2*n+1) // 6
        sum_arr = 0
        sumsq_arr = 0

        for num  in arr:
            sum_arr += num
            sumsq_arr += num*num

        val1 = sum_arr - sum_natural
        val2 = sumsq_arr - sumsq_natural

        val2 = val2/val1
        x=  (val1+val2)//2
        y = x- val1

        return[int(x), int(y)]
 
    #time = O(n) , #space = O(1)

