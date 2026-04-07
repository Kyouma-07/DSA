import math

class Armstrong:

        def __init__(self):
         pass

        def checkArmstrong(self, n: int) -> bool:
           #calculating the number of digits in the given number:
           count = int(math.log10(n) +1)

           #checking for armstrong
           sum = 0
           temp = n 
           while  temp > 0:
               lastdigit = temp%10
               sum += lastdigit**count
               temp = temp//10       

           return sum == n           

if __name__ == "__main__":
     n = int(input("Enter the number :"))
     armstrong = Armstrong()
     res = armstrong.checkArmstrong(n)
     if res:
         print(f"{n} is an armstrong number:")
     else:
         print(f"{n} is not an armstrong number:")