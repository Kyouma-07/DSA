class LC50:

    def __init__(self):
        pass


    #iterative
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            x = 1 / x
            n = -n

        result = 1

        while n > 0:

            #odd result no (taken out power)
            if n % 2 == 1:
                result *= x

            #increase the exponent (current power chunk)
            x *= x
            #decrease the n (chunk size)
            n //= 2

        return result

    #recursive:
    def myPow1(self, x: float, n: int) -> float:

        if n < 0:
            x = 1 / x
            n = -n
        
        return self.pawoh( x, n)
        
    
    def pawoh(self, x : float, n : int):
        
        if n == 0:
            return 1
        
        half = self.pawoh(x, n//2)

        if n % 2 == 0:
            return half*half
        else:
            return half*half*x