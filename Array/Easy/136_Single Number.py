class LC136:

    def __init__(self):
        pass

    def singleNum(self, arr : list[int]):

        hashmap = {}

        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for i in hashmap:
            if hashmap[i] == 1:
                return  i
        #Time = 0(n) , space = 0(n)
        
    def singleNumXOR (self, arr : list[int]):

        res = 0
        for i in range(len(arr)):
            res = arr[i] ^ res
        
        return res

if __name__ == "__main__":
    print("hello world")
    obj = LC136()
    print(obj.singleNumXOR([2,2,1,1,3,3,4]))