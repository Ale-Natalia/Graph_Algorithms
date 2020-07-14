from graph import Graph

class UndirectedGraph(Graph):
    def __init__(self, numberOfVertices = 0, numberOfEdges = 0):
        super().__init__(numberOfVertices, numberOfEdges)

    def addEdge(self, vertex1, vertex2, cost = 0):
        '''
        two edges are added for the directed graph representation: one from vertex1 to vertex2 and one from vertex2 to vertex1
        '''
        Graph.addEdge(self, vertex1, vertex2, cost)
        Graph.addEdge(self, vertex2, vertex1, cost)

    def removeEdge(self, vertex1, vertex2):
        '''
        both edges are removed (both ways)
        '''
        Graph.removeEdge(vertex1, vertex2)
        Graph.removeEdge(vertex2, vertex1)