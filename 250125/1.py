import matplotlib.pyplot as plt
from collections import deque
import time


# Example graph (city map)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F', 'H'],
    'H': ['G']
}


# Bi-directional BFS
def bidirectional_bfs(graph, start, goal):
    if start == goal:
        return [start]

    frontier_start = deque([start])
    frontier_goal = deque([goal])

    visited_start = {start: None}
    visited_goal = {goal: None}

    while frontier_start and frontier_goal:
        # Expand from start side
        if frontier_start:
            node = frontier_start.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited_start:
                    visited_start[neighbor] = node
                    frontier_start.append(neighbor)
                    if neighbor in visited_goal:
                        return reconstruct_path(visited_start, visited_goal, neighbor)

        # Expand from goal side
        if frontier_goal:
            node = frontier_goal.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited_goal:
                    visited_goal[neighbor] = node
                    frontier_goal.append(neighbor)
                    if neighbor in visited_start:
                        return reconstruct_path(visited_start, visited_goal, neighbor)

    return None


def reconstruct_path(visited_start, visited_goal, meeting_point):
    path_start = []
    path_goal = []

    node = meeting_point
    while node is not None:
        path_start.append(node)
        node = visited_start[node]
    path_start.reverse()

    node = meeting_point
    while node is not None:
        path_goal.append(node)
        node = visited_goal[node]

    return path_start + path_goal[1:]


# Standard BFS
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

    return None


# DFS
def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path)
            if result:
                return result

    path.pop()
    return None


# Visualization
def visualize_graph(graph, path):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10)

    if path:
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="red", width=2)

    plt.show()


# Main Execution
start = 'A'
goal = 'H'

# Bi-directional BFS
start_time = time.time()
bidirectional_path = bidirectional_bfs(graph, start, goal)
bidirectional_time = time.time() - start_time
print("Bi-directional BFS Path:", bidirectional_path)
print("Time Taken (Bi-directional BFS):", bidirectional_time)

# Standard BFS
start_time = time.time()
bfs_path = bfs(graph, start, goal)
bfs_time = time.time() - start_time
print("Standard BFS Path:", bfs_path)
print("Time Taken (Standard BFS):", bfs_time)

# DFS
start_time = time.time()
dfs_path = dfs(graph, start, goal)
dfs_time = time.time() - start_time
print("DFS Path:", dfs_path)
print("Time Taken (DFS):", dfs_time)

# Visualize the graph and paths
print("\nVisualizing Bi-directional BFS Path...")
visualize_graph(graph, bidirectional_path)

print("\nVisualizing Standard BFS Path...")
visualize_graph(graph, bfs_path)

print("\nVisualizing DFS Path...")
visualize_graph(graph, dfs_path)
