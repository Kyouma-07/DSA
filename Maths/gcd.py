class gcd:
    def __init__(self):
        pass

    def lcmAndGcd(self, a : int, b : int) -> list[int]:
        # code here
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        gcd = gcd(a,b)
        lcm = (a*b)//gcd
        return [lcm,gcd]
    
if __name__ == "__main__":
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second Number:"))
    gcd = gcd()
    res = gcd.lcmAndGcd(a,b)
    print(res)