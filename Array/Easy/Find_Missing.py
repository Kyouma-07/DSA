class Find_Missing:

    def __init__ (self):
        pass


    def brute(self, arr: list[int]):

        for i  in range (1, len(arr) +1):
            found = False
            for j in arr:
                if j == i:
                    found = True
                    break

            if not found:
                return i
    #time = 0(n^2)

    def optimalHashMap(self, arr: list[int]):

        hash = [0]* (len(arr) + 2 )

        for i in range(0,len(arr)):
            hash[arr[i]] += 1
        
        for i in range (1 , len(arr)+ 2):
            if hash[i] == 0:
                return i
            
    def optimalSum(self, arr: list[int]):
        n= len(arr) + 1

        total_sum = n*(n+1)//2
        actual_sum = sum(arr)

        return total_sum - actual_sum

    def optimalXOR(self, arr: list[int]):
        n = len(arr) +1

        xor_all = 0
        xor_arr = 0

        for i in range(n-1):
            xor_arr ^= arr[i]
            xor_all  ^= i+1
        
        xor_all ^= n

        return xor_all ^ xor_arr

if __name__ ==  "__main__":
    print("hello world!!")
    obj = Find_Missing()
    print(obj.optimalXOR([-1,1,0, 2, 0 , 4, 0, 5, 9, 10, 0]))
        
    