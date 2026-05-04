class LC485:

    def __init__ (self):
        pass

    def maxOnes(self,arr: list[int]) -> int:

        max_One = 0
        counter = 0

        for i in arr:
            if i == 1:
                counter += 1
                max_One = max(max_One, counter)
            else:
                counter = 0
        
        return max_One

if __name__ == "__main__":
    print("hello world")
    obj = LC485()
    print(obj.maxOnes([1,1,0,1,1,1]))