class GraphColor:

    def __init__(self):
        self.all_valid_colorings = []

    def isValid(self, vertex, color, adj):
        for neighbour in adj[vertex]:
            if color[neighbour] == color[vertex]:
                return False

        return True

    def generateCombo(self, vertex, n, m, adj, color):

        # All vertices colored
        if vertex == n:
            self.all_valid_colorings.append(color.copy())
            return

        # Try every color
        for c in range(1, m + 1):

            color[vertex] = c

            if self.isValid(vertex, color, adj):
                self.generateCombo(
                    vertex + 1,
                    n,
                    m,
                    adj,
                    color
                )

            # Backtrack
            color[vertex] = 0

    def graphColoring(self, n, m, edges):

        self.all_valid_colorings = []

        # Build adjacency list
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        color = [0] * n

        self.generateCombo(
            0,
            n,
            m,
            adj,
            color
        )

        return self.all_valid_colorings




    def graphColoring1(self, n, m, edges):

        # Build adjacency list
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        color = [0] * n

        def is_valid1(vertex, c):
            for neighbor in adj[vertex]:
                if color[neighbor] == c:
                    return False

            return True

        def dfs1(vertex):

            # All vertices colored
            if vertex == n:
                self.all_valid_colorings.append(color.copy())
                return

            for c in range(1, m + 1):

                if is_valid1(vertex, c):

                    color[vertex] = c

                    dfs1(vertex + 1)

                    # Backtrack
                    color[vertex] = 0

        dfs1(0)

        return self.all_valid_colorings

if __name__ == "__main__":

    n = 4
    m = 3

    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (0, 2)
    ]

    obj = GraphColor()

    print(obj.graphColoring(n, m , edges))