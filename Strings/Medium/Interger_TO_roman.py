class LC8:
    def intToRoman(self, num: int) -> str:

        #ask -> what is the largest ROMAN numerial i can subtract:
        #store the mapping as a list[tuple()] , 

        #using dict , we need to sort it first, so we avoid it:
        #usign greddy approach , we subtract biggest possible numbers

        #Store every valid Roman numeral, including the subtractive ones.

        roman = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        result = []

        for value, symbol in roman:
            while num >= value:
                result.append(symbol)
                num -= value

        return "".join(result)