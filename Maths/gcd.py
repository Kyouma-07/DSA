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
    
    # "using  iterative approach"
    def lcmAndGcdIterative(self, a: int, b: int) -> list[int]:
        def gcd_iterative(a, b):
            while b:
                a, b = b, a % b
            return a
        gcd = gcd_iterative(a, b)
        lcm = (a * b) // gcd
        return [lcm, gcd]

if __name__ == "__main__":
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second Number:"))
    gcd1 = gcd()
    res = gcd1.lcmAndGcd(a,b)
    print(res)