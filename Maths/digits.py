#counting the number of digits in a number

class MathConcepts:

    def __init__(self):
        pass

    def countDigits(self, n : int) -> int:
        count = 0
        while n > 0:
            count += 1
            n = n//10
        return count
    
        #cnt = int(math.log10(n) + 1) -> can calculate using this method as well:
        #time complexity  -> If n has d digits, then the loop runs d times
        #O(logn)
    
    def countDigits1(self, n : int) -> int:
        count = int(math.log10(n) + 1)
        return count
        #time complexity -> O(1)
        #space complexity -> O(1)

    def reverseDigits(self, n : int) -> int:
        rev = 0
        while n > 0:
            rev = rev*10 + n%10
            n = n//10
        return rev
        #time complexity -> O(logn) -> If n has d digits, then the loop runs d times

    def pritingDivisors(self, n : int) -> None:
        for i in range(1,n+1):
            if n%i == 0:
                print(i,end = " ")
        #time complexity -> O(n)
    
    def pritingDiviors1(self , n : int) ->None:
        i = 1
        while i*i <= n:  #(using i*i instead of sqrt(n)
            if n%i == 0:
                print(i,end = " ")
                if i != n//i:
                    print(n//i,end = " ")
            i += 1
        #time complexity -> O(sqrt(n))
        

if __name__ == "__main__":
    n = int(input("Enter the number:"))
    math = MathConcepts()
    res = math.countDigits(n)
    print(res)