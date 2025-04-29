from collections import deque
maze_2177 = [
    [1, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1],
]

ROWS_2177, COLS_2177 = len(maze_2177), len(maze_2177[0])
start_2177 = (0, 0)

def is_valid(r_2177, c_2177):
    return 0 <= r_2177 < ROWS_2177 and 0 <= c_2177 < COLS_2177 and maze_2177[r_2177][c_2177] == 1

def get_neighbors(r_2177, c_2177):
    for dr_2177, dc_2177 in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr_2177, nc_2177 = r_2177 + dr_2177, c_2177 + dc_2177
        if is_valid(nr_2177, nc_2177):
            yield (nr_2177, nc_2177)

def bfs(start_2177, goal_check):
    queue_2177 = deque([(start_2177, [start_2177])])
    visited_2177 = set()
    nodes_explored_2177 = 0

    while queue_2177:
        current_2177, path_2177 = queue_2177.popleft()
        if current_2177 in visited_2177:
            continue
        visited_2177.add(current_2177)
        nodes_explored_2177 += 1
        if goal_check(current_2177):
            return path_2177, nodes_explored_2177
        for neighbor_2177 in get_neighbors(*current_2177):
            queue_2177.append((neighbor_2177, path_2177 + [neighbor_2177]))
    return None, nodes_explored_2177

def dfs(start_2177, goal_check):
    stack_2177 = [(start_2177, [start_2177])]
    visited_2177 = set()
    nodes_explored_2177 = 0

    while stack_2177:
        current_2177, path_2177 = stack_2177.pop()
        if current_2177 in visited_2177:
            continue
        visited_2177.add(current_2177)
        nodes_explored_2177 += 1
        if goal_check(current_2177):
            return path_2177, nodes_explored_2177
        for neighbor_2177 in get_neighbors(*current_2177):
            stack_2177.append((neighbor_2177, path_2177 + [neighbor_2177]))
    return None, nodes_explored_2177

def dls(node_2177, path_2177, visited_2177, depth_2177, goal_check, nodes_explored_2177):
    if depth_2177 == 0:
        return (path_2177, nodes_explored_2177 + 1) if goal_check(node_2177) else (None, nodes_explored_2177 + 1)
    visited_2177.add(node_2177)
    nodes_explored_2177 += 1
    for neighbor_2177 in get_neighbors(*node_2177):
        if neighbor_2177 not in visited_2177:
            res_path_2177, nodes_explored_2177 = dls(neighbor_2177, path_2177 + [neighbor_2177], visited_2177.copy(), depth_2177 - 1, goal_check, nodes_explored_2177)
            if res_path_2177:
                return res_path_2177, nodes_explored_2177
    return None, nodes_explored_2177

def iddfs(start_2177, goal_check, max_depth_2177=30):
    for depth_2177 in range(max_depth_2177):
        visited_2177 = set()
        result_2177, nodes_explored_2177 = dls(start_2177, [start_2177], visited_2177, depth_2177, goal_check, 0)
        if result_2177:
            return result_2177, nodes_explored_2177
    return None, nodes_explored_2177

def is_rightmost(cell_2177):
    return cell_2177[1] == COLS_2177 - 1

def is_leftmost(cell_2177):
    return cell_2177[1] == 0 and cell_2177 != start_2177

def compare_algorithms():
    for desc_2177, goal_check in [("Rightmost Path", is_rightmost), ("Leftmost Path", is_leftmost)]:
        print(f"\n--- {desc_2177} ---")

        path_bfs_2177, nodes_bfs_2177 = bfs(start_2177, goal_check)
        print(f"BFS: Nodes Explored = {nodes_bfs_2177}, Path Length = {len(path_bfs_2177) if path_bfs_2177 else 'None'}")

        path_dfs_2177, nodes_dfs_2177 = dfs(start_2177, goal_check)
        print(f"DFS: Nodes Explored = {nodes_dfs_2177}, Path Length = {len(path_dfs_2177) if path_dfs_2177 else 'None'}")

        path_iddfs_2177, nodes_iddfs_2177 = iddfs(start_2177, goal_check)
        print(f"IDDFS: Nodes Explored = {nodes_iddfs_2177}, Path Length = {len(path_iddfs_2177) if path_iddfs_2177 else 'None'}")

compare_algorithms()