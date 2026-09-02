class LC1863:
    def subsetXORSum(self, nums: list[int]) -> int:
        total = 0


        #recursion - backtracking:
        def backtrack(index, current_xor):
            nonlocal total  #can modify local inside this function:

            #base-case
            if index == len(nums):
                total += current_xor
                return
            
            #choice  1: skip
            backtrack(index + 1, current_xor)

            #choice 2 : choose
            backtrack(index +1 , current_xor ^ nums[index])
        
        backtrack(0, 0)

        return total