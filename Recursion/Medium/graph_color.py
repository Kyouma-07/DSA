class GraphColor:
    def __init__(self):
        pass

    # Modified to only check edges connected to the current vertex
    def isValid(self, vertex: int, color: list[int], edges: list[tuple[int, int]]) -> bool:
        for u, v in edges:
            # If the edge connects to our current vertex, check the neighbor
            if u == vertex and color[v] != 0 and color[u] == color[v]:
                return False
            if v == vertex and color[u] != 0 and color[u] == color[v]:
                return False
        return True

    def generateCombo(self, vertex: int, n: int, m: int, edges: list[tuple[int, int]], color: list[int]) -> bool:
        # Base case: if we reach here, all prior early checks passed.
        if vertex == n:
            return True

        for i in range(1, m + 1):
            color[vertex] = i

            # EARLY PRUNING: Only recurse if the current color is actually valid
            if self.isValid(vertex, color, edges):
                if self.generateCombo(vertex + 1, n, m, edges, color):
                    return True
            

        return False

    def graphColoring(self, n: int, m: int, edges: list[tuple[int, int]]) -> list[int] | None:
        color = [0] * n
        if self.generateCombo(0, n, m, edges, color):
            return color
        return None



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