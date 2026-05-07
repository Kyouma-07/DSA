class LC1708:
    
    def __init__(self):
        pass

    def subarrayK(self, arr: list[int], target : int) -> int:

        freq ={ 0: -1}  # { current_sum : at what index we find this current_sum}
        current_sum = 0
        max_len = 0

        for i in range(len(arr)):

            current_sum += arr[i]
            need = current_sum - target

            if need in freq:
                max_len = max(max_len ,  i - freq[need])
            
            if current_sum not in freq:
                freq[current_sum] = i
            
        return max_len
            

if __name__ == "__main__":
    print("Hello world!!")
    obj = LC1708()
    print(obj.subarrayK([1,2,3,-3,1,1,1,4,2,-3], 3))
