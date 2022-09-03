

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        if vertex not in list(self.gdict):
            self.gdict[vertex] = []
        self.gdict[vertex].append(edge)

    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)
        if v in list(self.gdict):
            for i in self.gdict[v]:
                if i not in visited:
                    self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, v)
    
    def topologicalSort(self):

        visited = []
        stack = []

        #for k in list(self.gdict):
        for k in self.gdict.keys():
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)

        print(stack)

# customDict = {
#     "a": ["b", "c"],
#     "b": ["a", "d", "e"],
#     "c": ["a", "e"],
#     "d": ["b", "e", "f"],
#     "e": ["b", "d", "f"],
#     "f": ["d", "e"]
# }

graph = Graph()
graph.addEdge("A", "C")
graph.addEdge("C", "E")
graph.addEdge("E", "H")
graph.addEdge("E", "F")
graph.addEdge("F", "G")
graph.addEdge("B", "C")
graph.addEdge("B", "D")
graph.addEdge("D", "F")

# print(graph.gdict)
graph.topologicalSort()
