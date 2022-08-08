from collections import defaultdict

# Initializing the Graph Class
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance


def possible_mvt(pos):
    pList = [pos + 6, pos + 10, pos + 15, pos + 17, pos - 17, pos - 15, pos - 10, pos - 6]
    return [i for i in pList
            if ((i in range(0, 64)) and (pos % 8, i % 8) not in [(0, 7), (0, 6), (1, 7), (7, 1), (6, 0), (7, 0)])]

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    return visited, path

def solution(pos, des):
    graph = Graph()
    for i in range(64):
        graph.addNode(i)
    for i in range(64):
        for t in possible_mvt(i):
            graph.addEdge(i, t, 1)

    return dijkstra(graph, pos)[0][des]

