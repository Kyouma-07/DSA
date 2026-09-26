class Solution:
    def splitString(self, s: str) -> bool:
        
        def dfs(index, prev, count):

            if index == len(s):
                return count >= 2

            next_num = prev - 1

            for end in range(index + 1, len(s) + 1):

                current = s[index:end]

                if int(current) == next_num:
                    if dfs(end, next_num, count + 1):
                        return True

            return False

        for i in range(1, len(s)):

            first = int(s[:i])

            if dfs(i, first, 1):
                return True

        return False