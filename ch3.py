from queue import PriorityQueue


def possible_mvt(pos):
    pList = [pos + 6, pos + 10, pos + 15, pos + 17, pos - 17, pos - 15, pos - 10, pos - 6]
    return [i for i in pList
            if ((i in range(0, 64)) and (pos % 8, i % 8) not in [(0, 7), (0, 6), (1, 7), (7, 1), (6, 0), (7, 0)])]


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for _ in range(num_of_vertices)] for _ in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight


def dijkstra(graph, start_vertex):
    D = {v: float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


def solution(pos, des):
    g = Graph(64)
    for i in range(64):
        for t in possible_mvt(i):
            g.add_edge(i, t, 1)
    D = dijkstra(g, pos)
    return D[des]

print(solution(19, 36))