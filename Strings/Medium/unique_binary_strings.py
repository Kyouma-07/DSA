class LC1980:
    def findDifferentBinaryString(self, nums: list[str]):
        
        seen = set(nums)
        n = len(nums)

        for i in range( 2*n):
            binary =  bin(i)[2:]

            #add leading zeros if necessary
            while len(binary) < n:
               binary =  "0" + binary

            if binary not in seen:
                return binary