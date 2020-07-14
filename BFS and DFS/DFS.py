from undirected_graph import UndirectedGraph
from external_functions import *

def getArticulationPoints(graph, visitedArray, depthArray, lowPointArray, parentArray, vertex, depth):
    '''
    gets the articulation points
    '''
    visitedArray[vertex] = True
    depthArray[vertex] = depth
    lowPointArray[vertex] = depth
    numberofChildren = 0
    isArticualtion = False

    neighbours = graph.parseOutbound(vertex)
    for neighbour in neighbours:
        if not visitedArray[neighbour]:
            parentArray[neighbour] = vertex
            getArticulationPoints(graph, visitedArray, depthArray, lowPointArray, parentArray, neighbour, depth + 1)
            numberofChildren = numberofChildren + 1
            if lowPointArray[neighbour] >= depthArray[vertex]:
                isArticualtion = True
            lowPointArray[vertex] = min(lowPointArray[vertex], lowPointArray[neighbour])
        elif neighbour != parentArray[vertex]:
            lowPointArray[vertex] = min(lowPointArray[vertex], depthArray[neighbour])
    if (parentArray[vertex] is not None and isArticualtion) or (parentArray[vertex] is None and numberofChildren > 1):
        pass

class DFS(object):
    def __init__(self, graph):
        self._graph = graph
        self._discoveryTime = 0
        self._numberOfBCC = 0

    def findBCC(self, vertex, parents, lowPoints, discoveredArray, stack):
        numberOfChildren = 0
        discoveredArray[vertex] = self._discoveryTime
        lowPoints[vertex] = self._discoveryTime
        self._discoveryTime += 1

        neighbours = self._graph.parseOutbound(vertex)
        for neighbour in neighbours:
            if discoveredArray[neighbour] == -1:
                parents[neighbour] = vertex
                numberOfChildren += 1
                stack.append((vertex, neighbour))
                self.findBCC(neighbour, parents, lowPoints, discoveredArray, stack)

                lowPoints[vertex] = min(lowPoints[vertex], lowPoints[neighbour])

                if (parents[vertex] == -1 and numberOfChildren >= 2) or (parents[vertex] != -1 and lowPoints[neighbour] >= discoveredArray[vertex]):
                    self._numberOfBCC += 1
                    edge = -1
                    while edge != (vertex, neighbour):
                        edge = stack.pop()
                        print(edge)
                    print(" ")


            elif neighbour != parents[vertex] and lowPoints[vertex] > discoveredArray[neighbour]:
                lowPoints[vertex] = min(discoveredArray[neighbour], lowPoints[vertex])
                stack.append((vertex, neighbour))


    def DFSbiconnectedComponents(self, vertex):
        '''
        finds the biconnected components of a graph performing a DFS search
        :param graph: given graph
        return: a list of graphs represented as
        '''
        visitedArray = [False] * self._graph.NumberOfVertices
        discoveredArray = [-1] * self._graph.NumberOfVertices
        lowPoints = [-1] * self._graph.NumberOfVertices
        parents = [-1] * self._graph.NumberOfVertices
        stack = []

        for vertex in range(self._graph.NumberOfVertices):
            if discoveredArray[vertex] == -1:
                self.findBCC(vertex, parents, lowPoints, discoveredArray, stack)
            if stack:
                self._numberOfBCC += 1

                while stack:
                    edge = stack.pop()
                    print(edge)
                print(" ")


graph = readUndirectedGraph("lab2_bonus_ex.txt")
dfs = DFS(graph)
dfs.DFSbiconnectedComponents(0)