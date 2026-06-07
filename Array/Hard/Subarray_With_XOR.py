class Solution2:

    def __init__(self):
        pass


    
    def subarraysWithXorK(self, arr: list[int], target: int) -> int:
        
        freq = {0: 1}   #{PrefixXOR : frequency of this prefixXOR}
        counter = 0
        current_XOR = 0

        for i in arr:
            current_XOR ^= i
            need = current_XOR ^ target

            if need in freq:
                counter = counter + freq[need]

            if current_XOR in freq:
                freq[current_XOR] += 1
            else:
                freq[current_XOR] = 1


        return counter



