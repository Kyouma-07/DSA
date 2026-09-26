class HappyString:
    def getHappyString(self, n: int, k: int) -> str:
        
        def backtrack(path):
            nonlocal k

            if len(path) == n:
                k -= 1

                if k == 0:
                    return "".join(path)

                return ""

            for ch in "abc":
                if path and path[-1] == ch:
                    continue

                path.append(ch)
                ans = backtrack(path)
                path.pop()
                if ans:
                    return ans

            return ""

        return backtrack([])