class Solution:

    def __init__(self):
        pass

    def ZeroBrute(self, arr : list[int])-> list[int]:
        n= len(arr)
        temp = []
        for i in range(n):
            if arr[i] != 0:
                temp.append(arr[i])
        
        for i in range(len(temp)):
            arr[i] = temp[i]
        
        for i in range(len(temp), n):
            arr[i] = 0
        
        return arr
    
    def ZeroOptimal(self, arr: list[int]) -> list[int]:

        j= None

        #finding first zero 
        for i in range(len(arr)):
            if arr[i] == 0:
                j = i
                break
        
        #if no zero , return arr
        if j == None:
            return arr

        # moving non-zero element forward
        for i in range(j+1, len(arr)):
            if arr[i] != 0:
                arr[j], arr[i] = arr[i], arr[j]
                j += 1

        return arr
    
if __name__ ==  "__main__":
    print("hello world!!")
    obj = Solution()
    print(obj.ZeroOptimal([-1,1,0, 2, 0 , 4, 0, 5, 9, 10, 0]))