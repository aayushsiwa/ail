# Adjacency list for the graph
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D', 'G'],
    'D': ['E'],
    'E': ['F'],
    'F': [],
    'G': ['H', 'K'],
    'H': ['I'],
    'I': [],
    'J': [],
    'K': ['J', 'L'],
    'L': ['M'],
    'M': ['N'],
    'N': []
}

goal = 'N'

# BFS Implementation
def bfs(graph, start, goal):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node == goal:
                return visited  # Return nodes visited so far when goal is found
            queue.extend(graph[node])

    return visited  # If goal is not found, return all visited nodes


# DFS Implementation
def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == goal:
        return path  # Return the path instead of visited nodes

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path)
            if result:
                return result

    path.pop()  # Remove the node if no solution is found
    return None


# IDDFS Implementation
def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        path = []
        if dls(graph, start, goal, depth, visited, path):
            return path
    return None


def dls(graph, node, goal, depth, visited, path):
    visited.add(node)
    path.append(node)

    if depth == 0 and node == goal:
        return True
    if depth > 0:
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dls(graph, neighbor, goal, depth - 1, visited, path):
                    return True

    path.pop()  # Backtrack when no solution is found
    return False


# Comparing the searches
start = 'A'
goal = 'N'
max_depth = 10

print("BFS:", bfs(graph, start, goal))
print("DFS:", dfs(graph, start, goal))
print("IDDFS:", iddfs(graph, start, goal, max_depth))
