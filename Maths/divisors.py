import math
class Divisors:

    def __init__(self):
        pass

    def printDivisors(self, n:  int) -> list[int]:
        divisors = []
        for i in range (1, int(math.sqrt(n)) + 1, 1):
            if n%i == 0:
                divisors.append(i)
                if i != n//i:
                    divisors.append(n//i)
        return divisors
    
    def printPrimeDivisors(self, n: int) -> list[int]:
        primeDivisors = []
        for i in range(2, int(math.sqrt(n) +1)):
            if n%i == 0:
                primeDivisors.append(i)
                while n%i  == 0:
                    n= n//i
        if n > 1:
            primeDivisors.append(n)
        return primeDivisors

if __name__ == "__main__":
    n= int(input("Enter the number:"))
    divisor = Divisors()
    res = divisor.printPrimeDivisors(n)
    print(res)