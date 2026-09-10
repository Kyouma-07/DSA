def find_one_path(maze):
    n = len(maze)
    visited = [[False] * n for _ in range(n)]
    path = []

    def backtrack(r, c):
        # Invalid cell
        if r < 0 or r >= n or c < 0 or c >= n:
            return False

        if maze[r][c] == 0 or visited[r][c]:
            return False

        # Destination
        if r == n - 1 and c == n - 1:
            return True

        # Choose
        visited[r][c] = True

        # Down
        path.append("D")
        if backtrack(r + 1, c):
            return True
        path.pop()

        # Right
        path.append("R")
        if backtrack(r, c + 1):
            return True
        path.pop()

        # Up
        path.append("U")
        if backtrack(r - 1, c):
            return True
        path.pop()

        # Left
        path.append("L")
        if backtrack(r, c - 1):
            return True
        path.pop()

        return False

    if backtrack(0, 0):
        return "".join(path)

    return ""


def find_all_paths(maze):
    n = len(maze)
    visited = [[False] * n for _ in range(n)]

    path = []
    all_paths = []

    def backtrack(r, c):
        # Invalid cell
        if r < 0 or r >= n or c < 0 or c >= n:
            return

        if maze[r][c] == 0 or visited[r][c]:
            return

        # Destination
        if r == n - 1 and c == n - 1:
            all_paths.append("".join(path))
            return

        # Choose
        visited[r][c] = True

        # Down
        path.append("D")
        backtrack(r + 1, c)
        path.pop()

        # Right
        path.append("R")
        backtrack(r, c + 1)
        path.pop()

        # Up
        path.append("U")
        backtrack(r - 1, c)
        path.pop()

        # Left
        path.append("L")
        backtrack(r, c - 1)
        path.pop()

        # Undo
        visited[r][c] = False

    backtrack(0, 0)

    return all_paths


maze = [
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]

print(find_one_path(maze))
print(find_all_paths(maze))