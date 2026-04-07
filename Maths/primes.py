import math
class Prime:

    def __init__(self):
        pass

    def isPrime(self, n: int) -> bool:
        if n <= 1:
            return False
        for i in range (2, int(math.sqrt(n)) +1):
            if n % i == 0:
                return False
            break
        return True
    
    def countPrimes(self, m: int, n: int) -> list[int]:
        primes = []
        for i in range (m, n+1, 1):
            if self.isPrime(i):
                primes.append(i)
        return primes
    
if __name__ == "__main__":
    m = int(input("Enter the starting number:"))
    n = int(input("Enter the ending number:"))
    primes = Prime()
    res = primes.countPrimes(m,n)
    print(res)