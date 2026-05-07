class LC560:

    def __init__ (self):
        pass

    
    def subarraySum(self, arr : list[int], target: int) -> int:

        hash = { 0 : 1}  # { prefix_sum : frequency of how many times we find this prefix sum} => { prefix_sum 0 : seen once}
        counter = 0
        current_sum = 0

        for i in arr:
            current_sum += i
            need = current_sum - target

            if need in hash:
                counter = counter + hash[need]
            

            if current_sum in hash:
                hash[current_sum] += 1
            else:
                hash[current_sum] = 1
        
        return counter

if __name__ == "__main__":
    print("Hello world!!")
    obj = LC560()
    print(obj.subarraySum([1,2,3,-3,1,1,1,4,2,-3], 3))