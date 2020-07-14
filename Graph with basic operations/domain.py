class Edge(object):
    def __init__(self, vertex1, vertex2, cost,  id = None):
        self._vertex1 = vertex1
        self._vertex2 = vertex2
        self._cost = cost
        self._id = id

    @property
    def Vertex1(self):
        return self._vertex1

    @property
    def Vertex2(self):
        return self._vertex2

    @property
    def Cost(self):
        return self._cost

    @property
    def ID(self):
        return self._id

    def __eq__(self, other):
        return self._vertex1 == other.Vertex1 and self._vertex2 == other.Vertex2

class Vertex(object):
    def __init__(self, id):
        self._id = id

    @property
    def ID(self):
        return self._id

class VertexRelation(object):
    '''
    class used for defining the relations of a vertex
    it contains a list of in vertices (the vertices FROM which there exist edges to the given vertex)
                a list of out edges (the vertices TO which there exist edges to the given vertex)
    '''
    def __init__(self):
        self._inVertices = []
        self._outVertices = []

    @property
    def InVertices(self):
        return self._inVertices

    @property
    def OutVertices(self):
        return self._outVertices

    @InVertices.setter
    def InVertices(self, other):
        self._inVertices = other

    @OutVertices.setter
    def OutVertices(self, other):
        self._outVertices = other