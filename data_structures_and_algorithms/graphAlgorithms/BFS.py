# BFS is an algorithm for traversing Graph data structures. 
#   It starts at some arbituary node of a graph and explores the neighbour nodes
#   It starts at current level first, and then moves to next level neighbors
from linkedListQueue import Queue

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

customDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["c", "b", "d", "f"],
    "f": ["d", "e"]
}

graph = Graph(customDict)
graph.bfs("b")