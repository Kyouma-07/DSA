class LC2375:
    def smallestNumber(self, pattern: str) -> str:
        
        stack = []
        ans = []

        for i in range(len(pattern) + 1):

            # Push next smallest digit
            stack.append(i + 1)

            # If we see I, or reach the end,
            # empty the stack
            if i == len(pattern) or pattern[i] == 'I':

                while stack:
                    ans.append(stack.pop())

        return ''.join(map(str, ans))




    def smallestNumber2(self, pattern: str) -> str:
        result = []
        used = [False] * 10
        n = len(pattern)

        def backtrack(index : int):
            
            #base-case
            if index  == n + 1:
                return True
            
            #try digits
            for digit in range(1 , 10):

                if used[digit]:
                    continue
                
                if index > 0:
                    prev = result[-1]

                    if pattern[index-1] == "I" and  prev >= digit:
                        continue
                    if pattern[index - 1] == "D" and prev <= digit:
                        continue
                
                #choose
                result.append(digit)
                used[digit] = True

                #explore
                if backtrack(index + 1):
                    return True
                
                #undo:
                result.pop()
                used[digit] = False

            return False
        
        backtrack(0)

        return "".join(map(str,result))