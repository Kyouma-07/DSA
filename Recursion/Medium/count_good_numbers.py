class LC1922:

    def __init__(self):
        pass



    def countGoodNumbers(self, n: int) -> int:
        #number of even-index positions = (n + 1) // 2
        #number of odd-index positions = n // 2

        #answer = 5 ^ ((n + 1) // 2) × 4 ^ (n // 2)
        MOD = 10**9 + 7
        even_count = (n + 1) // 2
        odd_count = n // 2

        even_part = self.power(5, even_count)
        odd_part = self.power(4, odd_count)

        return (even_part * odd_part) % MOD

    #recursive:

    def power1(self,base : int, exp : int):
            result = 1
            MOD = 10**9 + 7

            if exp == 0:
                return 1

            half = self.power(base, exp //2)

            if exp % 2 == 1:
                return (half*half)*base % MOD
            else:
                return (half*half) % MOD

    #iterative:
    def power(self,base : int, exp : int):
            result = 1
            MOD = 10**9 + 7

            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % MOD

                base = (base * base) % MOD
                exp //= 2

            return result