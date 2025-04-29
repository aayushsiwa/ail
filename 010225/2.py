import heapq
import numpy as np

goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])


def get_neighbors(state):
    state = np.array(state)
    row, col = np.where(state == 0)[0][0], np.where(state == 0)[1][0]
    moves = []
    directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

    for direction, (dr, dc) in directions.items():
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = state.copy()
            new_state[row, col], new_state[new_row, new_col] = (
                new_state[new_row, new_col],
                new_state[row, col],
            )
            moves.append((new_state.tolist(), direction))

    return moves


def h1(state):
    return sum(
        1
        for i in range(3)
        for j in range(3)
        if state[i][j] != goal_state[i][j] and state[i][j] != 0
    )


def h2(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_x, goal_y = np.where(goal_state == state[i][j])
                distance += abs(i - goal_x[0]) + abs(j - goal_y[0])
    return distance


def a_star(start_state, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_state, []))
    visited = set()
    cost_so_far = {str(start_state): 0}

    while priority_queue:
        _, current_state, path = heapq.heappop(priority_queue)
        current_tuple = tuple(map(tuple, current_state))

        if np.array_equal(current_state, goal_state):
            return path, len(visited)

        if current_tuple in visited:
            continue
        visited.add(current_tuple)

        for neighbor, move in get_neighbors(current_state):
            new_cost = cost_so_far[str(current_state)] + 1
            if (
                str(neighbor) not in cost_so_far
                or new_cost < cost_so_far[str(neighbor)]
            ):
                cost_so_far[str(neighbor)] = new_cost
                priority = new_cost + heuristic(neighbor)
                heapq.heappush(priority_queue, (priority, neighbor, path + [move]))

    return None, len(visited)


# Example Start State (Shuffled)
start_state = [[1, 2, 3], [4, 0, 5], [6, 8, 7]]

# Run A* with H1 (Misplaced Tiles)
path1, explored1 = a_star(start_state, h1)

# Run A* with H2 (Manhattan Distance)
path2, explored2 = a_star(start_state, h2)

# Results
print(f"H1 (Misplaced Tiles) → Moves: {path1}, Nodes Explored: {explored1}")
print(f"H2 (Manhattan Distance) → Moves: {path2}, Nodes Explored: {explored2}")
