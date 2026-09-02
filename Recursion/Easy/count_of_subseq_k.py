class countSubseq:

    def __init__ (self):
            pass    


    def sumSub(self, arr :  list[int], target: int):
              
        self.arr = arr
        self.target = target
        self.count = 0
        self.backtrack(0, 0, [])

        return self.count


    def backtrack(self, index : int,  current_sum: int,  path: list[int]):

        #base:
        if index == len(self.arr):
             if current_sum == self.target and len(path) > 0:
                  self.count += 1
                  return
             else:
                  return

        #choice 1: skip
        self.backtrack(index +1 , current_sum , path)

        #choice 2: take
        path.append(self.arr[index])
        #explore:
        self.backtrack(index+1 , current_sum + self.arr[index] , path)
        #undo
        path.pop()