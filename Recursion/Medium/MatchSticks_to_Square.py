class MatchSticks:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total // 4

        matchsticks.sort(reverse=True)

        sides = [0, 0, 0, 0]

        def backtrack(index):

            if index == len(matchsticks):
                return True

            stick = matchsticks[index]

            seen = set()

            for i in range(4):

                if sides[i] in seen:
                    continue

                seen.add(sides[i])

                if sides[i] + stick > target:
                    continue

                sides[i] += stick

                if backtrack(index + 1):
                    return True

                sides[i] -= stick

            return False

        return backtrack(0)