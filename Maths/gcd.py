class gcd:
    def __init__(self):
        pass

    def lcmAndGcd(self, a : int, b : int) -> list[int]:
        # code here
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        gcd = gcd(a,b) # type: ignore
        lcm = (a*b)//gcd # type: ignore
        return [lcm,gcd] # type: ignore
    
if __name__ == "__main__":
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second Number:"))
    gcd1 = gcd()
    res = gcd1.lcmAndGcd(a,b)
    print(res)