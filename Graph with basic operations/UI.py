from external_functions import readGraph, writeGraph, writeGraphConsole, randomGraph
from graph import Graph

class UI:
    def __init__(self):
        self._graph = None
        pass

    def printMainMenu(self):
        print("1. Create new empty graph")
        print("2. Create random graph")
        print("3. Read a graph from a text file")
        print("4. Exit")

    def printGraphOperationsMenu(self):
        print("1. Add vertex")
        print("2. Remove vertex")
        print("3. Add/modify an edge")
        print("4. Remove an edge")
        print("5. Get the in degree of a vertex")
        print("6. Get the out degree of a vertex")
        print("7. Parse the set of inbound edges of a vertex")
        print("8. Parse the set of outbound edges of a vertex")
        print("9. Get the cost of an edge")
        print("10. Write the graph to a text file")
        print("11. Print graph to console")
        print("12. Exit")

    def validateVerticesAndEdges(self, numberOfVertices, numberOfEdges):
        if numberOfVertices < 0:
            raise ValueError("Number of vertices must be >=0")
        if numberOfEdges < 0:
            raise ValueError("Number of edges must be >=0")
        if numberOfEdges > numberOfVertices * (numberOfVertices - 1):
            raise ValueError("The number of edges is at most numberOfVertices * (numberOfVertices - 1)")

    def createEmptyGraph(self):
        self._graph = Graph()

    def createRandomGraph(self):
        try:
            numberOfVertices = int(input("Number of vertices: "))
            numberOfEdges = int(input("Number of edges: "))
        except ValueError:
            print("Numbers must be integers")
            return
        try:
            self.validateVerticesAndEdges(numberOfVertices, numberOfEdges)
        except ValueError as error:
            print(error)
            return
        self._graph = randomGraph(numberOfVertices, numberOfEdges)

    def createGraphFromTextfile(self):
        file = input("Text file: ")
        try:
            self._graph = readGraph(file)
        except ValueError as error:
            print(error)

    def addVertex(self):
        try:
            vertex = int(input("Vertex: "))
        except ValueError:
            print("Number must be integer")
        try:
            added = self._graph.addVertex(vertex)
            if added:
                print("Vertex successfully added")
            else:
                print("Vertex already exists")
        except ValueError as error:
            print(error)

    def removeVertex(self):
        try:
            vertex = int(input("Vertex: "))
        except ValueError:
            print("Number must be integer")
        removed = self._graph.removeVertex(vertex)
        if removed:
            print("Vertex successfully removed")
        else:
            print("Vertex does not exist")

    def addModifyEdge(self):
        try:
            vertex1 = int(input("Vertex 1: "))
            vertex2 = int(input("Vertex 2: "))
            cost = int(input("Cost: "))
        except ValueError:
            print("Numbers must be integers")
            return
        try:
            self._graph.addEdge(vertex1, vertex2, cost)
            print("Edge successfully added/modified")
        except ValueError as error:
            print(error)

    def removeEdge(self):
        try:
            vertex1 = int(input("Vertex 1: "))
            vertex2 = int(input("Vertex 2: "))
        except ValueError:
            print("Numbers must be integers")
            return
        removed = self._graph.removeEdge(vertex1, vertex2)
        if removed:
            print("Edge successfully removed")
        else:
            print("Edge does not exist")

    def getInDegree(self):
        try:
            vertex = int(input("Vertex: "))
        except ValueError:
            print("Number must be integer")
            return
        inDegree = self._graph.inDegree(vertex)
        if inDegree is not None:
            print("In degree of vertex " + str(vertex) + " is " + str(inDegree))
        else:
            print("Vertex does not exist")

    def getOutDegree(self):
        try:
            vertex = int(input("Vertex: "))
        except ValueError:
            print("Number must be integer")
            return
        outDegree = self._graph.outDegree(vertex)
        if outDegree is not None:
            print("Out degree of vertex " + str(vertex) + " is " + str(outDegree))
        else:
            print("Vertex does not exist")

    def inboundEdges(self):
        try:
            vertex = int(input("Vertex: "))
        except ValueError:
            print("Number must be integer")
            return
        edges = self._graph.parseInbound(vertex)
        if edges is not None:
            string = ""
            for edge in edges:
                string += str(edge) + " " + str(vertex) + ", cost: " + str(self._graph.Costs[(edge, vertex)]) + "\n"
            print("Inbound edges of vertex " + str(vertex) + ":\n" + string)
        else:
            print("Vertex does not exist")

    def outboundEdges(self):
        try:
            vertex = int(input("Vertex: "))
        except ValueError:
            print("Number must be integer")
            return
        edges = self._graph.parseOutbound(vertex)
        if edges is not None:
            string = ""
            for edge in edges:
                string += str(vertex) + " " + str(edge) + ", cost: " + str(self._graph.Costs[(vertex, edge)]) + "\n"
            print("Outbound edges of vertex " + str(vertex) + ":\n" + string)
        else:
            print("Vertex does not exist")

    def cost(self):
        try:
            vertex1 = int(input("Vertex 1: "))
            vertex2 = int(input("Vertex 2: "))
        except ValueError:
            print("Numbers must be integers")
            return
        cost = self._graph.findEdgeBetweenVertices(vertex1, vertex2)
        if cost is not None:
            print("The cost is " + str(cost))
        else:
            print("The edge does not exist")

    def writeGraph(self):
        file = input("File name: ")
        if(file[-4:] != ".txt"):
            print("File name must end in .txt")
            return
        writeGraph(self._graph, file)
        print("Graph written to file")

    def printGraph(self):
        writeGraphConsole(self._graph)

    def run(self):
        graphCreated = False
        while not graphCreated:
            self.printMainMenu()
            try:
                choice = int(input("Make your choice: "))
                if choice == 1:
                    self.createEmptyGraph()
                elif choice == 2:
                    self.createRandomGraph()
                elif choice == 3:
                    self.createGraphFromTextfile()
                elif choice == 4:
                    return
                else:
                    print("Choice must be 1-4")
            except ValueError:
                print("Choice must be 1-4")
            graphCreated = self._graph is not None
        while True:
            self.printGraphOperationsMenu()
            try:
                choice = int(input("Make your choice: "))
                if choice == 1:
                    self.addVertex()
                elif choice == 2:
                    self.removeVertex()
                elif choice == 3:
                    self.addModifyEdge()
                elif choice == 4:
                    self.removeEdge()
                elif choice == 5:
                    self.getInDegree()
                elif choice == 6:
                    self.getOutDegree()
                elif choice == 7:
                    self.inboundEdges()
                elif choice == 8:
                    self.outboundEdges()
                elif choice == 9:
                    self.cost()
                elif choice == 10:
                    self.writeGraph()
                elif choice == 11:
                    self.printGraph()
                elif choice == 12:
                    return
                else:
                    print("Choice must be 1-12")
            except ValueError:
                print("Choice must be 1-12")

'''
graph = readGraph("graph_read.txt")
writeGraph(graph, "graph_write.txt")

running = True
while running:
    numberOfVertices = int(input("Number of vertices: "))
    numberOfEdges = int(input("Number of edges: "))
    random_graph = randomGraph(numberOfVertices, numberOfEdges)
    writeGraphConsole(random_graph)
'''