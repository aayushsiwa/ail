def bfs_shortest_path(grid, start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(grid), len(grid[0])
    queue = [(*start, 0)]
    visited = set([start])
    nodes_explored = 0

    while queue:
        row, col, dist = queue.pop(0)
        nodes_explored += 1

        if (row, col) == end:
            return dist, nodes_explored

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and grid[new_row][new_col] == 1
                and (new_row, new_col) not in visited
            ):
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))

    return -1, nodes_explored


def dfs_find_path(grid, start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(grid), len(grid[0])
    stack = [start]
    visited = set([start])
    nodes_explored = 0

    while stack:
        row, col = stack.pop()
        nodes_explored += 1

        if (row, col) == end:
            return True, nodes_explored

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and grid[new_row][new_col] == 1
                and (new_row, new_col) not in visited
            ):
                visited.add((new_row, new_col))
                stack.append((new_row, new_col))

    return False, nodes_explored


grid = [
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1],
]
start = (2, 0)
end = (4, 3)

bfs_distance, bfs_nodes = bfs_shortest_path(grid, start, end)
print(f"BFS: Shortest path distance = {bfs_distance}, Nodes explored = {bfs_nodes}")

dfs_valid, dfs_nodes = dfs_find_path(grid, start, end)
print(f"DFS: Found valid path = {dfs_valid}, Nodes explored = {dfs_nodes}")

print(f"Comparison: BFS explored {bfs_nodes} nodes, DFS explored {dfs_nodes} nodes.")
