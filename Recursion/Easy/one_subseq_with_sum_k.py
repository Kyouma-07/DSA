
class oneSum:

    def __init__(self):
        pass


    def sumSub(self, arr :  list[int], target: int):
        self.result = []
        self.arr = arr
        self.target = target
        self.backtrack(0, 0, [])

        return self.result


    def backtrack(self, index : int,  current_sum: int,  path: list[int]):


        if current_sum == self.target and len(path) > 0:
            self.result.append(path[:])
            return True

        #base:
        if index == len(self.arr):
            return False
        
        #choice 1: skip
        if self.backtrack(index +1 , current_sum , path):
            return True

        #choice 2: take
        path.append(self.arr[index])
        #explore:
        if self.backtrack(index+1 , current_sum + self.arr[index] , path):
            return True
        #undo
        path.pop()

        return False