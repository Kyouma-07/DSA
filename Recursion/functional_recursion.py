class FuncRecursion:

    def __init__(self):
        pass

    #printing 1 to N
    def oneToN(self, n : int):
        if n == 0:
            return 
        self.oneToN(n-1)
        print(n)

    #printing N to 1
    def nToOne(self, count : int):
        if count == 0:
            return
        print(count)
        self.nToOne(count-1)
    

    #sum of first N numbers
    def sumOfN(self, n : int) -> int:
        if n == 0:
            return 0
        return n + self.sumOfN(n-1)
    
    #factorial of a number:
    def facto(self, n: int) -> int:
        if n == 0:
            return 1
        return n * self.facto(n-1)
    
    #reversing array ) two-pointers
    def arrayrev(self, arr : list[int], left: int, right: int) -> list[int]:
        if left >= right:
            return arr
        else:
            arr[left], arr[right] = arr[right], arr[left]
            return self.arrayrev(arr, left+1, right-1)
        
    #reversing array ( single index)
    def arrayrev2(self, arr : list[int],i , n ) ->list[int]:
        if i >= n//2:
            return arr
        else:
            arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
            return self.arrayrev2(arr,i+1, n)

    #string plaindrome
    def palindrome(self, string: str, left: int, right: int) -> bool:
        if left >= right:
            return True
        if string[left] != string[right]:
            return False
        else:
            return self.palindrome(string, left+1, right-1)
        
    #plaindrome number
    def palindromeNumber(self, number: int, rev: int , original: int)->bool:
        if number < 0:
            return False
        if number == 0:
            return rev == original
        return self.palindromeNumber(number//10,rev*10 + number%10, original)
    
    
    #plaindrom without extra space
    def isPalindrome(self, n: int)-> bool:
        if n < 0:
            return False
        left = [n]

        def helper(right):
            #base condition
            if right == 0:
                return True
            
            if not helper(right//10):
                return False
            
            if left[0]%10 != right%10:
                return False
            
            left[0] //= 10
            return True
        
        return helper(n)
    
    #fibonaci with functional recursion
    def fibo(self, number: int) -> int:
        if number == 0:
            return 0
        return self.fibo(number-1) + self.fibo(number - 2)
    #time =2^n (same values recomputed many times)

    #with optimization
    def fiboMemo(self, number: int, dp=None):
        if dp is None:
            dp = {}
     
        if number <= 1:
            return number
        
        if number in dp:
            return dp[number]
        # Recursive computation
        dp[number] = self.fiboMemo(number - 1, dp) + self.fiboMemo(number - 2, dp)
        
        return dp[number]




if __name__ == "__main__":
    print("hello world")

    obj = FuncRecursion()
    print(obj.palindromeNumber(153,0,153))