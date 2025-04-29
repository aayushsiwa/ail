import heapq
import numpy as np
import time

class PuzzleState:
    def __init__(self, board, parent=None, move="", g=0, heuristic="manhattan"):
        self.board = board
        self.parent = parent
        self.move = move
        self.g = g  
        self.h = self.compute_heuristic(heuristic)
        self.f = self.g + self.h  
        self.heuristic_type = heuristic

    def __lt__(self, other):
        return self.f < other.f  

    def __eq__(self, other):
        return np.array_equal(self.board, other.board)

    def compute_heuristic(self, heuristic):
        if heuristic == "manhattan":
            return self.manhattan_distance()
        elif heuristic == "misplaced":
            return self.misplaced_tiles()
        return 0

    def manhattan_distance(self):
        goal_positions = {val: (i // 3, i % 3) for i, val in enumerate(range(9))}
        distance = 0
        for i in range(3):
            for j in range(3):
                val = self.board[i][j]
                if val != 0:
                    goal_i, goal_j = goal_positions[val]
                    distance += abs(i - goal_i) + abs(j - goal_j)
        return distance

    def misplaced_tiles(self):
        goal = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        return np.sum(self.board != goal) - (1 if self.board[0, 0] != 0 else 0)

    def generate_neighbors(self):
        neighbors = []
        x, y = np.argwhere(self.board == 0)[0]
        moves = [("Up", x - 1, y), ("Down", x + 1, y), ("Left", x, y - 1), ("Right", x, y + 1)]

        for move, new_x, new_y in moves:
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = self.board.copy()
                new_board[x, y], new_board[new_x, new_y] = new_board[new_x, new_y], new_board[x, y]
                neighbors.append(PuzzleState(new_board, self, move, self.g + 1, self.heuristic_type))
        return neighbors

def solve_puzzle(initial_board, heuristic="manhattan", algorithm="A*"):
    start_time = time.time()
    start = PuzzleState(np.array(initial_board), heuristic=heuristic)
    goal_state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

    open_list = []
    heapq.heappush(open_list, start)
    closed_set = set()
    nodes_expanded = 0

    while open_list:
        current = heapq.heappop(open_list)
        nodes_expanded += 1

        if np.array_equal(current.board, goal_state):
            path = []
            while current.parent:
                path.append(current.move)
                current = current.parent
            execution_time = time.time() - start_time
            return list(reversed(path)), nodes_expanded, execution_time

        closed_set.add(current.board.tobytes())

        for neighbor in current.generate_neighbors():
            if neighbor.board.tobytes() in closed_set:
                continue

            if algorithm == "GBFS":
                neighbor.f = neighbor.h  

            heapq.heappush(open_list, neighbor)

    return None, nodes_expanded, time.time() - start_time  # No solution found

def hill_climbing(initial_board, heuristic="manhattan"):
    start_time = time.time()
    current = PuzzleState(np.array(initial_board), heuristic=heuristic)
    nodes_expanded = 0

    while True:
        neighbors = current.generate_neighbors()
        nodes_expanded += len(neighbors)
        if not neighbors:
            break

        best_neighbor = min(neighbors, key=lambda state: state.h)

        if best_neighbor.h >= current.h:  # Stop if no improvement
            execution_time = time.time() - start_time
            return None, nodes_expanded, execution_time

        current = best_neighbor

        if np.array_equal(current.board, np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])):
            execution_time = time.time() - start_time
            return [], nodes_expanded, execution_time  # Found solution

# Example usage
initial_board = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

astar_solution, astar_nodes, astar_time = solve_puzzle(initial_board, heuristic="manhattan", algorithm="A*")
gbfs_solution, gbfs_nodes, gbfs_time = solve_puzzle(initial_board, heuristic="manhattan", algorithm="GBFS")
hill_solution, hill_nodes, hill_time = hill_climbing(initial_board, heuristic="manhattan")

print("\nA* Results:")
print("Solution:", astar_solution)
print("Nodes Expanded:", astar_nodes)
print("Execution Time:", astar_time, "seconds")

print("\nGreedy Best-First Search Results:")
print("Solution:", gbfs_solution)
print("Nodes Expanded:", gbfs_nodes)
print("Execution Time:", gbfs_time, "seconds")

print("\nHill Climbing Results:")
print("Solution Found:", hill_solution is not None)
print("Nodes Expanded:", hill_nodes)
print("Execution Time:", hill_time, "seconds")
