class powerexpo:

    def __init__(self):
        pass


    def calculatePower(self, x : float, n :  float) -> float:
        answer = 1

        if n < 0:
            x = 1/x
            n = -n

        while n > 0:
            if n%2 == 1:
                answer = answer*x
            x= x*x
            n= n//2

        #using bit manipulation.
        """     
        while n:
        if n & 1:
            answer *= x
        
        x *= x
        n >>= 1

        """
        return answer
    
       

if __name__ == "__main__":
    x = float(input("Enter the base:"))
    n = float(input("Enter the exponent:"))
    res = powerexpo()
    print(res.calculatePower(x,n))
