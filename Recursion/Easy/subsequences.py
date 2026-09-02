class Subsequences:

    def __init__(self):
        pass



    def subSequence( self, arr : list[int]):
        self.result = []
        self.arr = arr

        self.backtrack(0,[])
        return self.result

    def backtrack(self, index: int, current : list[int]):

        #base-case:
        if index == len(self.arr):
            self.result.append(current[:])
            return

        #choice 1: skip it
        self.backtrack(index + 1, current)

        #choice 2: keep it
        current.append(self.arr[index])
        #explore other choices:
        self.backtrack(index + 1, current)
        #pop
        current.pop()
