from math import inf
from copy import deepcopy
from graph import Graph
from external_functions import readGraph


class GraphMatrix(object):
    def __init__(self, givenGraph):
        self._adjacencyMatrix = []
        ''''''
        for vertex1 in range(givenGraph.NumberOfVertices):
            row = []
            for vertex2 in range(givenGraph.NumberOfVertices):
                if vertex1 is vertex2:
                    row.append(0)
                else:
                    row.append(inf)
            for vertex2 in givenGraph.parseOutbound(vertex1):
                try:
                    row[vertex2] = givenGraph.Costs[(vertex1, vertex2)]
                except:
                    pass
            self._adjacencyMatrix.append(row)

    @property
    def AdjacencyMatrix(self):
        return self._adjacencyMatrix

    @property
    def NumberOfVertices(self):
        return len(self._adjacencyMatrix)


class ShortCostWalkMatrixMultiplication(object):
    def __init__(self, givenGraph):
        self._n = givenGraph.NumberOfVertices
        self._w = givenGraph.AdjacencyMatrix
        self._d = deepcopy(self._w)
        self._walk = None
        self._valid = True
        self._initializeWalk()
        self._shortestCostWalk()

    def _initializeWalk(self):
        '''
        the walk matrix is initialized, each walk from i to j being initialized with [i, j]
        '''
        self._walk = []
        for i in range(self._n):
            walkRow = []
            for j in range(self._n):
                walkFromiToj = [i, j]
                walkRow.append(walkFromiToj)
            self._walk.append(walkRow)

    def _extend(self):
        '''
        the matrix d is extended, checking at each step for a better decomposition
        '''
        for i in range(self._n):
            for j in range(self._n):
                for k in range(self._n):
                    walk = self._walk[i][j]
                    if self._d[i][k] + self._w[k][j] < self._d[i][j]:
                        self._d[i][j] = self._d[i][k] + self._w[k][j]
                        self._walk[i][j] = self._walk[i][k] + [j]
                    #self._d[i][j] = min(self._d[i][j], self._d[i][k] + self._w[k][j])

    def _shortestCostWalk(self):
        '''
        the d matrix is extended up to the power n-1
        '''
        for m in range(1, self._n-1):
            self._extend()
        self._setValid()

    def _setValid(self):
        '''
        the graph is valid if there are no negative cycles and invalid otherwise
        '''
        for i in range(self._n):
            if self._d[i][i] != 0:
                self._valid = False
                break

    def getShortestCostWalkBetweenTwoVertices(self, vertex1, vertex2):
        if self._valid:
            return self._walk[vertex1][vertex2], self._d[vertex1][vertex2]
        else:
            return "The graph has negative cycles"


graph_ex = readGraph("graph.txt")
graph_ex = GraphMatrix(graph_ex)
shortCostWalk = ShortCostWalkMatrixMultiplication(graph_ex)
print(shortCostWalk.getShortestCostWalkBetweenTwoVertices(0, 1))

graph_ex = readGraph("graph2.txt")
graph_ex = GraphMatrix(graph_ex)
shortCostWalk = ShortCostWalkMatrixMultiplication(graph_ex)
print(shortCostWalk.getShortestCostWalkBetweenTwoVertices(0, 2))

graph_ex = readGraph("graph_negative_cycles.txt")
graph_ex = GraphMatrix(graph_ex)
shortCostWalk = ShortCostWalkMatrixMultiplication(graph_ex)
print(shortCostWalk.getShortestCostWalkBetweenTwoVertices(0, 1))