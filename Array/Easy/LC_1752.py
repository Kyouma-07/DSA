class LC1752:

    def __init__(self):
        pass
    
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        drops = 0

        for i in range(n):
            if nums[i] > nums[ (i+1) % n]:
                drops += 1
                if drops > 1:
                    return False
        return True

if __name__ == "__main__":
    print("hello world!!")
    obj = LC1752()
    print(obj.check([2,1,3,4]))