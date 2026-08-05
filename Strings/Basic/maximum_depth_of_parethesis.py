class LC1614:
    def maxDepth(self, s: str) -> int:

        depth = 0
        max_depth = 0

        for i in s:
            if i == "(":
                depth += 1
                max_depth = max(max_depth, depth)

            elif i == ")":
                depth -= 1
            else:
                continue
        
        return max_depth
            