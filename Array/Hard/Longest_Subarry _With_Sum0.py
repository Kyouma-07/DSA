class Solution1:

    def __init__(self):
        pass


    def subarraySum0 (self, arr: list[int]) -> int:
        n= len(arr)
        freq ={ 0: -1}   #{prefix_sum :  index at which it is found}
        max_len = 0
        current_sum = 0

        for i in range(n):
            current_sum += arr[i]
        
            if current_sum in freq:
                max_len = max(max_len , i - freq[current_sum])
            else:
                freq[current_sum] = i

        return max_len