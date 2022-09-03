# DFS is an algorithm for traversing a graph data structure which startselecting
#   some arbituary node and explores as far as possible along each edge before backtracking
from linkedListQueue import Queue

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def dfs(self, vertex):
        # 1) create a visited list and a stack with the vertex
        # 2) loop while stack is not empty
        # 3) pop a vertex from thee stack
        # 4) loop through it's adjacent verticies
        # 5) check if the evertice has been visited
        # 6) if not, add it to the evisiteed list and add it to the stack
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
    "e": ["c", "b", "d", "f"],
    "f": ["d", "e"]
}

graph = Graph(customDict)
graph.dfs("a")