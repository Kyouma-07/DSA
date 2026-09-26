class GraphColor:

    def __init__(self):
        pass

    def isValid(self, color: list[int], edges: list[tuple[int, int]]) -> bool:
        for u, v in edges:
            if color[u] == color[v]:
                return False
        return True

    def generateCombo(self, vertex: int, n: int, m: int, edges: list[tuple[int, int]], color: list[int]) -> bool:
        # base-case: if all are colored, check for validity:
        if vertex == n:
            return self.isValid(color, edges)

        # try every color for this node:
        for i in range(1, m + 1):
            # save the color:
            color[vertex] = i

            # move to next vertex:
            if self.generateCombo(vertex + 1, n, m, edges, color):
                return True
            
            # backtrack : explicity overwrite
            color[vertex] = 0

        # if fail
        return False

    # Modified to return the list of colors, or None if it fails
    def graphColoring(self, n: int, m: int, edges: list[tuple[int, int]]) -> list[int] | None:
        color = [0] * n
        
        # If it returns True, the color array holds the winning combination
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
    result = obj.graphColoring(n, m, edges)
    
    if result:
        print(f"Success! The coloring is: {result}")
        for node, c in enumerate(result):
            print(f"Node {node} -> Color {c}")
    else:
        print("No valid coloring exists for this graph with the given number of colors.")