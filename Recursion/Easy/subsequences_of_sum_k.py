class subSequencesSum:

    def __init__(self):
        pass


    def sumSub(self, arr :  list[int], target: int):
        self.result = []
        self.arr = arr
        self.target = target
        self.backtrack(0, [])

        return self.result


    def backtrack(self, index : int,    current: list[int]):

        #base:
        if index == len(self.arr):
            if sum(current) == self.target:
                self.result.append(current[:])
                return
            else:
                return

        #choice 1: skip
        self.backtrack(index +1 , current)

        #choice 2: take
        current.append(self.arr[index])
        #explore:
        self.backtrack(index+1 , current)
        #undo
        current.pop()

    def backtrack2(self, index : int,    current: list[int]):

        #base:
        if sum(current) == self.target:
            self.result.append(current[:])


        for index in range(index ,len(self.arr)):
            #choice 2: take
            current.append(self.arr[index])
            #explore:
            self.backtrack2(index+1 , current)
            #undo
            current.pop()