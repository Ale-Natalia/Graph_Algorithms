from graph import Graph
from external_functions import randomGraph, writeGraphConsole

def reconstructPath(nextArray, startingVertex, endingVertex):
    '''
    reconstructs the minimum length path between two vertices in a directed graph, given the array of "next" vertices and the starting and ending vertex
    :param nextArray: the array of "next" elements
    :param startingVertex: the starting vertex
    :param endingVertex: the ending vertex
    return: the reconstructed path
            None if a path does not exist
    '''
    path = []
    path.append(startingVertex)
    destination = startingVertex
    while destination != endingVertex:
        if destination == -1:
            return None
        startingVertex = destination
        destination = nextArray[startingVertex]
        path.append(destination)
    return path

def backwardsBreadthFirstSearch(graph, startingVertex, endingVertex):
    '''
    breadth first search algorithm
    :param graph: the given graph
    :param startingVertex: the starting vertex
    :param endingVertex: the ending vertex
    return: the path
            None if there is no path
    '''
    if not (graph.findVertex(startingVertex) and graph.findVertex(endingVertex)):
        raise ValueError("Vertices must be consecutive positive numbers")
    if startingVertex == endingVertex:
        if graph.findEdgeBetweenVertices(startingVertex, endingVertex):
            return [startingVertex, endingVertex]
        else:
            return None
    visited = [False] * graph.NumberOfVertices # we keep track of the visited vertices so that we only visit each vertex once
    queue = [] # a queue of the vertices whose inbound neighbours we need to parse
    next = [-1] * graph.NumberOfVertices # we store the next vertex of each parsed vertex such that we can reconstruct the path
    queue.append(endingVertex)
    visited[endingVertex] = True

    while queue:
        vertex = queue.pop(0)
        for inbound in graph.parseInbound(vertex):
            if not visited[inbound]:
                queue.append(inbound)
                visited[inbound] = True
                next[inbound] = vertex

    return reconstructPath(next, startingVertex, endingVertex)

def minimumPathLength(graph, startingVertex, endingVertex):
    '''
    :param graph: the given graph
    :param startingVertex: the starting vertex
    :param endingVertex: the ending vertex
    return: the length of the path
    '''
    path = backwardsBreadthFirstSearch(graph, startingVertex, endingVertex)
    if path is None:
        return 0
    return len(path)

def stringMinimumLengthPath(graph, startingVertex, endingVertex):
    '''
    returns the minimum length path as a string
    '''
    string = ""
    path = backwardsBreadthFirstSearch(graph, startingVertex, endingVertex)
    length = minimumPathLength(graph, startingVertex, endingVertex)
    if path is None:
        return "Path does not exist"
    string += "The minimum length path of length " + str(length) + " is:\n"
    for vertex in path:
        string += str(vertex) + " -> "
    string = string[:-4]
    return string


'''
#graph = randomGraph(7, 15)
graph = Graph(5, 10)
graph.addEdge(0, 1)
graph.addEdge(1, 2)
graph.addEdge(2, 4)
graph.addEdge(2, 3)
graph.addEdge(3, 4)
graph.addEdge(1, 4)
graph.addEdge(0, 3)
graph.addEdge(0, 4)


writeGraphConsole(graph)
start = int(input("Start vertex: "))
end = int(input("End vertex: "))
print(stringMinimumLengthPath(graph, start, end))
backwardsBreadthFirstSearch(graph, start, end)
'''