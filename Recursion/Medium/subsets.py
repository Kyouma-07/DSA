class LC78:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        self.result = []
        self.nums = nums

        self.backtrack(0,[])
        return self.result

    def backtrack(self, index: int ,current : list[int]):
        
        #base-case
        if len(self.nums) == index:
            self.result.append(current.copy())
            return
        
        #choice 1: skip
        self.backtrack(index + 1, current)

        #choice 2: choose
        current.append(self.nums[index])
        self.backtrack(index + 1, current)

        #pop
        current.pop()

    #iterative
    def subsets1(self, nums: list[int]) -> list[list[int]]:

        result = [[]]
        for num in nums:
                new_subsets = []

                for subset in result:
                    new_subsets.append(subset + [num])

                result.extend(new_subsets)

        return result

    #iterative
    def subsets2(self, nums: list[int]) -> list[list[int]]:

        result = [[]]
        for num in nums:
            
            size = len(result)
            for i in range(size):

                result.append(result[i] + [num])
                
        return result
