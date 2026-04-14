class Name:
    def __init__(self):
        pass

    #name N times
    def nameNTimes(self, name: str, n:int):
        if n == 0:
            return ""
        print(name)
        self.nameNTimes(name, n - 1)
    
    #time = O(n)
    #space = O(n)

    #Printing 1 to N
    def oneToN(self,count:int):
        if count == 0:
            return 
        self.oneToN(count-1)
        print(count)
    #time = O(n)
    #space = O(n)


    #printing N to 1
    def nToOne (self, count : int):
        if count == 0:
            return
        print(count)
        self.nToOne(count-1)
    #time = O(n)
    #space = O(n)


    #printing sum of first N numbers.
    def sumOfN (self, count : int, sum : int):
        if count == 0:
            print(sum)
            return
        self.sumOfN(count-1, sum + count)
    #time = O(n)
    #space = O(n)


    #factorial of a number:
    def factorial(self, count: int, fact: int ):
        if count  == 0:
            print(fact)
            return
        self.factorial(count-1, fact*count)
    #time = O(n)
    #space = O(n)


    #reverse an array in place using recursion
    def arrayrev(self, arr: list[int], left : int, right : int):
        if left >= right:
            print(arr)   #note we can print it outside the function, this is just for solving the question 
            return #print outside the function in main when you want to use the array or pass it somewhere
        else:
            arr[left], arr[right] = arr[right], arr[left]
            self.arrayrev(arr, left+1, right-1)
    #time = O(n)
    #space = O(n)


    #check whethere the string is palindrome using recursion
    def palindromestr(self, string: str, left :int, right: int):
        if left >= right:
            print("True")
            return
        if string[left] != string[right]:
            print("False")
            return
        else:
            return self.palindromestr(string,left+1, right-1)
        #can use simple self.function name cause nothing is being returned back to function.
    #time = O(n)
    #space = O(n)


    #printing all elements of an array using recursion
    def printelements(self, arr: list[int], left: int , right: int):
        if left > right:
            return
        print(arr[left], "\n")
        return self.printelements(arr, left+1 , right)
    #time = O(n)
    #space = O(n)

    #palindrome for numbers using recursion
    def palindromeNumber(self, number: int, rev: int, original: int):
        if number < 0:
            print("False")
            return
        if number == 0:
            print(rev == original)
            return
        return self.palindromeNumber(number//10, rev * 10 + (number %10),original)
    #time = O(n)
    #space = O(n)
    

    #palindrome using recursion without using extra space.
    def palindromrecursion(self, n: int):
        if n < 0:
            print("Not Palindrome")
            return
        
        left = [n] #parsing as list to access digits in number:

        def helperFunc(right):

            #base function
            if right == 0:
                return True
            
            if not helperFunc(right//10):
                return False
            
            if left[0]%10 != right%10:
                return False
            
            left[0] //= 10
            return True
        
        return helperFunc(n)
    

    #i did not code this, AI did
    #parlindrome using recursion and tuple unpacking
    def isPalindrome(self, n: int) -> bool:
        if n < 0:
            return False
        
        def helper(num):
            if num == 0:
                return True, n   # (status, left side)
            
            status, left = helper(num // 10)
            
            if not status:
                return False, left
            
            if left % 10 != num % 10:
                return False, left
            
            return True, left // 10
        
        result, _ = helper(n)
        return result


    #fibbonacci using recursion
    def fib_parameterized(self, n: int, a=0, b=1):
        # Base Case: If we've reached the index we want, return the current value
        if n == 0:
            return a
        if n == 1:
            return b
        return self.fib_parameterized(n - 1, b, a + b)




if __name__ == "__main__":
    #name1 = int(input("Enter the name:"))
    count = int(input("Enter the number of times you want this Printed:"))
    obj = Name()
    print(obj.fib_parameterized(5,0,1))




"""9. Print all subsequences of a string

👉 Parameters:

index

current string

10. Print sum of all subsequences

👉 Parameters:

index

current sum"""