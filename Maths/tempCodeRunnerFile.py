        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        gcd = gcd(a,b)
        lcm = (a*b)//gcd
        return [lcm,gcd]