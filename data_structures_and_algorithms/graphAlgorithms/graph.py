
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        # searches throough the nearest vertexes first
        # array of already visited verticies
        visited = [vertex]
        # queue to store the adjacent verticies
        queue = [vertex]
        # while queue is not empty
        while queue:
            # dequeued vertex
            deVertex = queue.pop(0)
            # output the vertex
            print(deVertex)
            # for the adjacent verticies of the dequeued vertex
            for adjacentVertex in self.gdict[deVertex]:
                # if the vertex has not been visited
                if adjacentVertex not in visited:
                    # add vertex to the list of visited
                    visited.append(adjacentVertex)
                    # add vertex to the queue
                    queue.append(adjacentVertex)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            deVertex = stack.pop()
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)



    def newDFS(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)

customDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["b", "d", "f"],
    "f": ["d", "e"]
}

graph = Graph(customDict)
graph.addEdge("e", "c")
print(graph.gdict)