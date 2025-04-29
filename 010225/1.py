import heapq
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, cost):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, cost))
        self.graph[v].append((u, cost))

    def uniform_cost_search(self, start, goal):
        priority_queue = [(0, start)]
        visited = {}
        parent = {start: None}

        while priority_queue:
            cost, node = heapq.heappop(priority_queue)

            if node in visited and visited[node] <= cost:
                continue

            visited[node] = cost
            if node == goal:
                return cost, self.reconstruct_path(parent, start, goal)

            for neighbor, edge_cost in self.graph.get(node, []):
                new_cost = cost + edge_cost
                if neighbor not in visited or new_cost < visited.get(neighbor, float("inf")):
                    heapq.heappush(priority_queue, (new_cost, neighbor))
                    parent[neighbor] = node

        return float("inf"), []

    def reconstruct_path(self, parent, start, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        return path[::-1] if path[-1] == start else []


def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        visited.add(node)
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    return None


# Example
graph = Graph()
edges = [
    ("A", "B", 1), ("A", "C", 4),
    ("B", "D", 2), ("B", "E", 5),
    ("C", "F", 3),
    ("E", "F", 1)
]

for u, v, cost in edges:
    graph.add_edge(u, v, cost)

start, goal = "A", "F"

ucs_cost, ucs_path = graph.uniform_cost_search(start, goal)
bfs_path = bfs(graph.graph, start, goal)

print(f"UCS Optimal Path: {ucs_path}, Cost: {ucs_cost}")
print(f"BFS Path (Unweighted): {bfs_path}")
