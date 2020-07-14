from domain import Edge, VertexRelation
import copy

class Graph(object):
    '''
    abstract data type - graph
    '''
    def __init__(self, numberOfVertices = 0, numberOfEdges = 0):
        self._numberOfVertices = numberOfVertices
        self._numberOfEdges = numberOfEdges
        self._verticesInboundEdges = {} #key = vertex, value = a list of the vertices from which the inbound edges come
        self._verticesOutboundEdges = {} #key = vertex, value = a list of the vertices to which the outbound edges go
        self._costs = {} #key = tuple in/out vertices  of edge, value = cost

        for vertex in range(self._numberOfVertices):
            self._verticesInboundEdges.update({vertex: []})
            self._verticesOutboundEdges.update({vertex: []})

    @property
    def VerticesInboundEdges(self):
        return copy.deepcopy(self._verticesInboundEdges)

    @property
    def VerticesOutboundEdges(self):
        return copy.deepcopy(self._verticesOutboundEdges)

    '''
    @property
    def Edges(self):
        return self._edges
    '''

    @property
    def NumberOfVertices(self):
        return self._numberOfVertices

    @property
    def NumberOfEdges(self):
        return self._numberOfEdges

    @property
    def Costs(self):
        return copy.deepcopy(self._costs)

    '''
    @Edges.setter
    def Edges(self, other):
        self._edges = other
    '''
    def _updateVerticesAndEdges(self):
        '''
        updates the number of vertices and of edges after an operation that might modify them is performed
        :return: None
        '''
        self._numberOfVertices = len(self._verticesInboundEdges)
        self._numberOfEdges = len(self._costs)

    def findVertex(self, givenVertex):
        '''
        searches for vertex in graph
        :param givenVertex: given vertex to search
        :return: True - found
                 False - not found
        '''
        if givenVertex in self._verticesInboundEdges:
            return True
        return False

    def edgesWithVertex(self, vertex): #DO WE NEED THIS?
        '''
        returns a list of the edges that contain a given vertex
        :param vertex: given vertex
        :return: list of edges
        '''
        listOfEdges = []
        for edge in self._edges:
            if vertex in [self._edges[edge].Vertex1, self._edges[edge].Vertex2]:
                listOfEdges.append(self._edges[edge])
        return listOfEdges

    def edgeHasVertex(self, edge, vertex): #DO WE NEED THIS?
        '''
        determines if a given edge contains a given vertex
        :param edge: given edge
        :param vertex: given vertex
        :return: True/False
        '''
        if vertex in [edge.Vertex1, edge.Vertex2]:
            return True
        return False

    def addVertex(self, vertex):
        '''
        adds vertex to graph
        :param vertex: vertex to add
        :return: True - it was added
                 False - it already exists, so nothing happens
                 raises ValueError if the value of the vertex is too big
        '''
        if vertex > self._numberOfVertices:
            raise ValueError("Vertices must be consecutive positive numbers")
        if self.findVertex(vertex):
            return False
        self._verticesInboundEdges.update({vertex: []})
        self._verticesOutboundEdges.update({vertex: []})
        self._updateVerticesAndEdges()
        return True

    def removeVertex(self, givenVertex):
        '''
        removes vertex and associated edges from graph, as well as the costs of the edges
        decrements the value of the vertices greater than the removed vertex
        :param givenVertex: vertex to remove
        :return: True - it was removed
                 False - it couldn't be removed because it didn't exist
        '''
        if givenVertex in self._verticesInboundEdges:
            associatedInVertices = self._verticesInboundEdges[givenVertex]
            associatedOutVertices = self._verticesOutboundEdges[givenVertex]
        else:
            return False
        del self._verticesInboundEdges[givenVertex]
        del self._verticesOutboundEdges[givenVertex]

        for vertex in associatedInVertices:
            self._verticesOutboundEdges[vertex].remove(givenVertex)

        for vertex in associatedOutVertices:
            self._verticesInboundEdges[vertex].remove(givenVertex)

        #update costs dictionary - decrease vertices value
        updatedEdges = [] # list of tuples (vertex1, vertex2, cost) to update
        deletedEdges = [] # list of edges to delete
        for edge in self._costs:
            if edge[0] == givenVertex or edge[1] == givenVertex:
                deletedEdges.append(edge)
            else:
                vertex1 = edge[0]
                vertex2 = edge[1]
                cost = self._costs[edge]
                changed = False
                if vertex1 > givenVertex:
                    vertex1 -= 1
                    changed = True
                if vertex2 > givenVertex:
                    vertex2 -= 1
                    changed = True
                if changed:
                    deletedEdges.append((edge[0], edge[1]))
                    updatedEdges.append((vertex1, vertex2, cost))
        #delete edges
        for edge in deletedEdges:
            del self._costs[edge]
        #update edges
        for edge in updatedEdges:
            vertex1 = edge[0]
            vertex2 = edge[1]
            cost = edge[2]
            self._costs.update({(vertex1, vertex2): cost})

        #update inbound edges dictionary - decrease vertices value
        updatedEdges = [] #tuples vertex, list of inbound edges
        deletedEdges = [] #vertices to remove from dictionaries (as keys)
        for vertex in self._verticesInboundEdges:
            modified = False
            newVertex = vertex
            updatedListOfInbounds = copy.deepcopy(self._verticesInboundEdges[vertex])
            for index in range(len(updatedListOfInbounds)):
                if updatedListOfInbounds[index] > givenVertex:
                    updatedListOfInbounds[index] -= 1
                    modified = True
            if vertex > givenVertex:
                newVertex = vertex - 1
                modified = True
            if modified:
                deletedEdges.append(vertex)
                updatedEdges.append((newVertex, updatedListOfInbounds))
        #delete
        for vertex in deletedEdges:
            del self._verticesInboundEdges[vertex]
        #update
        for vertex in updatedEdges:
            self._verticesInboundEdges.update({vertex[0]: vertex[1]})

        # update outbound edges dictionary - decrease vertices value
        updatedEdges = []  # tuples vertex, list of inbound edges
        deletedEdges = []  # vertices to remove from dictionaries (as keys)
        for vertex in self._verticesOutboundEdges:
            modified = False
            newVertex = vertex
            updatedListOfOutbounds = copy.deepcopy(self._verticesOutboundEdges[vertex])
            for index in range(len(updatedListOfOutbounds)):
                if updatedListOfOutbounds[index] > givenVertex:
                    updatedListOfOutbounds[index] -= 1
                    modified = True
            if vertex > givenVertex:
                newVertex = vertex - 1
                modified = True
            if modified:
                deletedEdges.append(vertex)
                updatedEdges.append((newVertex, updatedListOfOutbounds))
        # delete
        for vertex in deletedEdges:
            del self._verticesOutboundEdges[vertex]
        # update
        for vertex in updatedEdges:
            self._verticesOutboundEdges.update({vertex[0]: vertex[1]})

        self._updateVerticesAndEdges()
        return True

    def addEdge(self, vertex1, vertex2, cost):
        '''
        adds edge going from vertex1 to vertex2 to the graph
        if the vertices do not exist, they are also added
        if the edge already exists, it is overwritten
        :param vertex1: first vertex (from) of edge to add
        :param vertex2: second vertex (to) of edge to add
        :param cost: cost of edge to add
        :return: None
                 raises ValueError if the edge to add has vertices with values that are too big
        '''
        if (vertex1 > self._numberOfVertices or vertex2 > self._numberOfVertices or vertex1 < 0 or vertex2 < 0) and not ((vertex1 == self._numberOfVertices and vertex2 == vertex1 + 1) or (vertex2 == self._numberOfVertices and vertex1 == vertex2 + 1)):
            raise ValueError("The vertices must be consecutive positive numbers")
        if vertex1 not in self._verticesOutboundEdges:
            self._verticesOutboundEdges.update({vertex1: [vertex2]})
        if vertex2 not in self._verticesInboundEdges:
            self._verticesInboundEdges.update({vertex2: [vertex1]})

        if vertex2 not in self._verticesOutboundEdges[vertex1]:
            self._verticesOutboundEdges[vertex1].append(vertex2)
        if vertex1 not in self._verticesInboundEdges[vertex2]:
            self._verticesInboundEdges[vertex2].append(vertex1)

        if (vertex1, vertex2) in self._costs:
            self._costs[(vertex1, vertex2)] = cost
        else:
            self._costs.update({(vertex1, vertex2): cost})

        self._updateVerticesAndEdges()

    def removeEdge(self, vertex1, vertex2):
        '''
        removes edge from vertex1 to vertex2
        :param vertex1: first vertex (from) of edge to add
        :param vertex2: second vertex (to) of edge to add
        :return: True - it was removed
                 False - it couldn't be removed because it didn't exist
        '''
        keyToSearch = (vertex1, vertex2)
        if keyToSearch in self._costs:
            del self._costs[keyToSearch]
            self._verticesInboundEdges[vertex2].remove(vertex1)
            self._verticesOutboundEdges[vertex1].remove(vertex2)
            self._updateVerticesAndEdges()
            return True
        return False

    def findEdgeBetweenVertices(self, vertex1, vertex2):
        '''
        searches for edge between two given vertices
        :param vertex1 - first vertex
        :param vertex2 - second vertex
        :return: the cost - edge was found
                 False - edge was not found
        '''
        if (vertex1, vertex2) in self._costs:
            return self._costs[(vertex1, vertex2)]
        return None

    def inDegree(self, vertex):
        '''
        gets the in degree of the given vertex
        :param vertex: the given vertex
        :return: the in degree of the given vertex
                 None if the vertex doesn't exist
        '''
        try:
            return len(self._verticesInboundEdges[vertex])
        except KeyError:
            return None

    def outDegree(self, vertex):
        '''
        gets the out degree of the given vertex
        :param vertex: the given vertex
        :return: the out degree of the given vertex
                 None if the vertex doesn't exist
        '''
        try:
            return len(self._verticesOutboundEdges[vertex])
        except KeyError:
            return None

    def parseInbound(self, vertex):
        '''
        returns an iterable with the inbound edges of a vertex
        :param vertex: given vertex
        :return: the iterable
                 None if vertex does not exist
        '''
        try:
            return self._verticesInboundEdges[vertex]
        except KeyError:
            return None

    def parseOutbound(self, vertex):
        '''
        returns an iterable with the outbound edges of a vertex
        :param vertex: given vertex
        :return: the iterable
                 None if vertex does not exist
        '''
        try:
            return self._verticesOutboundEdges[vertex]
        except KeyError:
            return None

    @staticmethod
    def copyGraph(graph):
        '''
        creates a deep copy of the graph
        :param graph: given graph
        :return: the created copy of the graph
        '''
        return copy.deepcopy(graph)