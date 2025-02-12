class Bitwise:

    def __init__(self):
        pass

    
    """ 
    #Bitwise AND in pyhton    a and b ( where a and b are operands, "and" is a bitwise operator)
    returns the bitwise AND of the two numbers. (when two output are true , it returns true)
    usecase: to check if a number is even or odd without using modulo operator
    when we AND 1 with any numbers digits remain the same. 
    
    #Bitwise OR in pyhton    a or b ( where a and b are operands, "or" is a bitwise operator)
    returns the bitwise OR of the two numbers. (when one of the output is true , it returns true)
    
    #XOR in pyhton    a ^ b ( where a and b are operands, "^" is a bitwise operator)
    XOR stands for exclusive OR. It returns true when the two inputs are different.
    if we XOR 1 with any number, it will flip the number. (complement of the number)

    
    Number System:
    1- Decimal Number system - Have a base 10 -> 0, 1,2, 3, 4, 5, 6, 7, 8, 9
    2- Binary Number system - Have a base 2 -> 0, 1
    3- Octal Number system - Have a base 8 -> 0, 1, 2, 3, 4, 5, 6, 7
    
    Number System Conversion:
    1- Decimal to Base b -> keep dividing by base b and keep the remainders and write in opposite order
    2- Base b to Decimal -> multiply each digit with base power of its position and add them all.

    
    left shift operators :- <<  (shifts the bits to the left by n places)
    10 in binary is 1010, 10 << 1 will be 10100 which is 20 in decimal.
    it actually boils down to multiplying the number by 2^n where n is the number of places shifted.
    general observation  [ a << b = a * 2^b ]

    right shift operators :- >>  (shifts the bits to the right by n places)
    10 in binary is 1010, 10 >> 1 will be 101 which is 5 in decimal.
    it actually boils down to dividing the number by 2^n where n is the number of places shifted.
    general observation  [ a >> b = a / 2^b ]

    Note :- leading zeros are ignored in all number systems.

    """

    #Question -> Given a number n , find out if the number is an even or odd number:
    
    @staticmethod
    def isEven(n: int) -> bool:

        """ 
        example -> 10011 (all numbers except the last digit are ignored because they are all even numbers)
        so if the last digit in base 2 is 1, then the number is odd else it is even.
        n AND 1 == 1 -> odd number , n AND 1 == 0 -> even number

        """
        return n & 1 == 0
    
    #Question -> Given an array of numbers , it contains the numbers and negative of that number, only 1 number is present by itself. Find that number.
    #example - [ -1, -2, -3, -4, 1, 2, 3, 4,5] -> -4 , use brute force method (add all )

    @staticmethod
    def findSingleNumber(nums: list) -> int:
        result = 0
        for num in nums:
            result += num
        return result



    #Question -> Given an array of numbers, every number occurs twice except one number, find that number.
    #example - [ 1, 2, 3, 4, 1, 2, 3] -> 4 , use brute force method and  then XOR method to solve this problem.

    @staticmethod
    def findunique(nums: list) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
    

    #Question -> Find the ith bit of a number n. where i is the position of the bit.
    #we can use masking to find the ith bit of a number n with n-1 zeros
    # n & (1 << n-1) -> will return the number instead of the digit  , hence we use the   (n >> (i - 1)) & 1
    #Extracts the i-th bit (from the right, 1-based indexing) of the number n.
    #or extract the i-th bit and right shift it to LSB.


    @staticmethod
    def findithBit(n: int, i: int) -> int:
        #return (n >> (i - 1)) & 1
        return (n & (1 << (i - 1))) >> (i - 1)



    #Question -> Set the ith bit of a number n. where i is the position of the bit. (set means turn it to 1)
    #we can use masking to set the ith bit of a number n with n-1 zeros, just or it with 1.

    @staticmethod
    def setithBit(n :int , i: int) -> int:
        return ( n | ( 1 << (i-1)) )


    #Question -> reset ith Bit ( if 1 then 0 , vice versa)
    #use the & operator  using a mask ^^

    @staticmethod
    def resetithBit( n: int , i: int) -> int:
        #mask the bit to ith place , invert the mask  (so the other digit remains unchanged during & operation)
        return  ( n &  ~( 1 << (i-1)) )


    #Question -> Find the position of the rightmost set bit: 
    @staticmethod
    def getrightmostsetBit( n: int) ->int:
        if n == 0:
            return 0
        else:
            return n & -n
        
    #Question -> Given an array of numbers , each number is appearning odd number of times except for 1 number that is appearing only 1 number of time, find the given number.

    #using a hashmap:
    def find_unique_number(arr  : list[int]) -> int:
        freq = {}  # Step 1: Initialize hashmap
        for num in arr:
            freq[num] = freq.get(num, 0) + 1  # Count occurrences

        for num, count in freq.items():  # Step 2: Find the number appearing once
            if count == 1:
                return num
    #time complexity 0(n) , space complexity 0(n)

    #using mathematical formula:
    #return (3 * sum(set(arr)) - sum(arr)) // 2
    #time complexity 0(n) , space complexity 0(n)
    


if __name__ == "__main__":
    bitwise = Bitwise()
    print(bitwise.isEven(10))
    print(bitwise.findSingleNumber( [ -1, -2, -3, -4, 1, 2, 3, 4,5]))
    print(bitwise.findunique( [ 1, 2, 3, 4, 1, 2, 3, 4,10]))
    print(bitwise.findithBit(10 , 3))
    print(bitwise.setithBit(10,1))
    print(bitwise.resetithBit(10,1))
    print(bitwise.getrightmostsetBit(10))