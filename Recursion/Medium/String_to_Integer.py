class LC80:

    def __init__(self):
        pass


    def myAtoi(self, s: str) -> int:

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        n = len(s)
        i = 0

        while i < n and s[i] == ' ':
            i += 1
        sign = 1

        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        def helper(i, num):
            if i == n or not s[i].isdigit():
                return sign * num

            digit = int(s[i])

            num = num * 10 + digit
            signed_num = sign * num

            if signed_num > INT_MAX:
                return INT_MAX

            if signed_num < INT_MIN:
                return INT_MIN

            return helper(i + 1, num)

        return helper(i, 0)