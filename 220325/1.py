import heapq


class Puzzle:
    def __init__(self, board, parent=None, move=None, depth=0, cost=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.zero_pos = self.find_zero()

    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def possible_moves(self):
        x, y = self.zero_pos
        moves = []
        directions = {"Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)}

        for move, (dx, dy) in directions.items():
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = (
                    new_board[new_x][new_y],
                    new_board[x][y],
                )
                moves.append(Puzzle(new_board, self, move, self.depth + 1))

        return moves

    def is_goal(self):
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))


def misplaced_tiles(puzzle):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return sum(
        1
        for i in range(3)
        for j in range(3)
        if puzzle.board[i][j] and puzzle.board[i][j] != goal[i][j]
    )


def manhattan_distance(puzzle):
    goal_positions = {
        n: (i, j)
        for i, row in enumerate([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        for j, n in enumerate(row)
    }
    return sum(
        abs(i - goal_positions[val][0]) + abs(j - goal_positions[val][1])
        for i, row in enumerate(puzzle.board)
        for j, val in enumerate(row)
        if val
    )


def search(initial_board, heuristic, search_type="A*"):
    initial_state = Puzzle(initial_board)
    frontier = []
    heapq.heappush(frontier, (heuristic(initial_state), initial_state))
    explored = set()

    while frontier:
        _, current = heapq.heappop(frontier)

        if current.is_goal():
            return reconstruct_path(current)

        explored.add(current)

        for neighbor in current.possible_moves():
            if neighbor in explored:
                continue

            neighbor.cost = (
                (neighbor.depth + heuristic(neighbor))
                if search_type == "A*"
                else heuristic(neighbor)
            )
            heapq.heappush(frontier, (neighbor.cost, neighbor))

    return None


def reconstruct_path(state):
    path = []
    while state.parent:
        path.append(state.move)
        state = state.parent
    return path[::-1]


# Example Usage
initial_board = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]

print("A* with Manhattan Distance:")
print(search(initial_board, manhattan_distance, "A*"))

print("Greedy BFS with Manhattan Distance:")
print(search(initial_board, manhattan_distance, "GBFS"))

print("A* with Misplaced Tiles:")
print(search(initial_board, misplaced_tiles, "A*"))

print("Greedy BFS with Misplaced Tiles:")
print(search(initial_board, misplaced_tiles, "GBFS"))
