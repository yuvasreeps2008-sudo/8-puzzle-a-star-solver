import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def misplaced_tiles(state):
    """Calculate number of misplaced tiles."""
    return sum(
        1 for i in range(9)
        if state[i] != 0 and state[i] != GOAL[i]
    )


def manhattan_distance(state):
    """Calculate Manhattan distance."""
    distance = 0

    for i, value in enumerate(state):
        if value != 0:
            current_row, current_col = divmod(i, 3)
            goal_row, goal_col = divmod(value - 1, 3)

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


def get_neighbors(state):
    """Generate all possible neighboring states."""
    neighbors = []

    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col

            new_state = list(state)
            new_state[blank], new_state[new_blank] = (
                new_state[new_blank],
                new_state[blank]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def a_star(start, heuristic):
    """Solve the puzzle using A* Search."""
    queue = []

    heapq.heappush(
        queue,
        (heuristic(start), 0, start, [])
    )

    cost = {start: 0}
    visited = set()
    nodes_expanded = 0

    while queue:
        f, g, current, path = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == GOAL:
            return path + [current], nodes_expanded

        for neighbor in get_neighbors(current):
            new_g = g + 1

            if neighbor not in cost or new_g < cost[neighbor]:
                cost[neighbor] = new_g
                new_f = new_g + heuristic(neighbor)

                heapq.heappush(
                    queue,
                    (new_f, new_g, neighbor, path + [current])
                )

    return None, nodes_expanded


def print_solution(path):
    """Display the solution steps."""
    for step, state in enumerate(path):
        print(f"Step {step}")

        for i in range(0, 9, 3):
            print(state[i:i + 3])

        print()


if __name__ == "__main__":

    start_state = (
        2, 8, 3,
        1, 6, 4,
        7, 0, 5
    )

    print("8-Puzzle Solver using A* Search")
    print("=" * 35)

    # Misplaced Tiles
    path1, expanded1 = a_star(
        start_state,
        misplaced_tiles
    )

    print("\nMisplaced Tiles Heuristic")
    print("Nodes Expanded:", expanded1)

    if path1:
        print("Solution Cost:", len(path1) - 1)

    # Manhattan Distance
    path2, expanded2 = a_star(
        start_state,
        manhattan_distance
    )

    print("\nManhattan Distance Heuristic")
    print("Nodes Expanded:", expanded2)

    if path2:
        print("Solution Cost:", len(path2) - 1)

    # Comparison
    print("\nHeuristic Comparison")
    print("=" * 35)
    print("Misplaced Tiles :", expanded1)
    print("Manhattan       :", expanded2)

    if expanded2 < expanded1:
        print("\nManhattan Distance expanded fewer nodes.")
        print("It is a more informed admissible heuristic.")

    print("\nSolution using Manhattan Distance:")
    print_solution(path2)
