class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        directions = {
            'L': (-1, 0),
            'R': (1, 0),
            'U': (0, 1),
            'D': (0, -1)
        }

        x = y = 0

        for move in moves:
            dx, dy = directions[move]
            x += dx
            y += dy

        return x == 0 and y == 0