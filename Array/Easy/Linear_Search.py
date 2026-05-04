class Linear_Search:

    def __init__ (self):
        pass

    def Linear(self, arr: list[int], num : int):

        for i in range(len(arr)):
            if arr[i] == num:
                return i
        
        return None

if __name__ == "__main__":
    print("hello world!!")
    obj = Linear_Search()
    print(obj.Linear([2,1,3,4],2))