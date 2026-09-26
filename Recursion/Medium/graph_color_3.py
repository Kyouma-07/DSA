class GraphColor:
    def __init__(self):
        self.all_valid_colorings = [] # Store all solutions here

    def isValid(self, vertex: int, color: list[int], edges: list[tuple[int, int]]) -> bool:
        for u, v in edges:
            if u == vertex and color[v] != 0 and color[u] == color[v]:
                return False
            if v == vertex and color[u] != 0 and color[u] == color[v]:
                return False
        return True

    def generateCombo(self, vertex: int, n: int, m: int, edges: list[tuple[int, int]], color: list[int]):
        # Base case: We found a valid coloring!
        if vertex == n:
            self.all_valid_colorings.append(list(color))
            return

        for i in range(1, m + 1):
            color[vertex] = i

            if self.isValid(vertex, color, edges):
    
                self.generateCombo(vertex + 1, n, m, edges, color)
            
            color[vertex] = 0

    def graphColoring(self, n: int, m: int, edges: list[tuple[int, int]]) -> list[list[int]]:
        color = [0] * n
        self.generateCombo(0, n, m, edges, color)
        return self.all_valid_colorings