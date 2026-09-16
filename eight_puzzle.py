import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def misplaced_tiles(state):
    return sum(
        1 for i in range(9)
        if state[i] != 0 and state[i] != GOAL[i]
    )


def manhattan_distance(state):
    distance = 0

    for i, value in enumerate(state):
        if value != 0:
            current_row, current_col = divmod(i, 3)
            goal_row, goal_col = divmod(value - 1, 3)
            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col
            new_state = list(state)

            new_state[zero], new_state[new_zero] = (
                new_state[new_zero],
                new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def a_star(start, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(start), 0, start, []))

    cost_so_far = {start: 0}
    expanded = set()
    nodes_expanded = 0

    while priority_queue:
        f, g, current, path = heapq.heappop(priority_queue)

        if current in expanded:
            continue

        expanded.add(current)
        nodes_expanded += 1

        if current == GOAL:
            return path + [current], nodes_expanded

        for neighbor in get_neighbors(current):
            new_g = g + 1

            if neighbor not in cost_so_far or new_g < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_g
                new_f = new_g + heuristic(neighbor)

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbor, path + [current])
                )

    return None, nodes_expanded


def print_solution(path):
    for step, state in enumerate(path):
        print(f"Step {step}:")
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
    print("--------------------------------")

    # Misplaced Tiles Heuristic
    path1, expanded1 = a_star(start_state, misplaced_tiles)

    print("\nMisplaced Tiles Heuristic")
    print("Nodes Expanded:", expanded1)

    if path1:
        print("Solution Cost:", len(path1) - 1)

    # Manhattan Distance Heuristic
    path2, expanded2 = a_star(start_state, manhattan_distance)

    print("\nManhattan Distance Heuristic")
    print("Nodes Expanded:", expanded2)

    if path2:
        print("Solution Cost:", len(path2) - 1)

    print("\nComparison")
    print("--------------------------------")
    print("Misplaced Tiles :", expanded1, "nodes expanded")
    print("Manhattan       :", expanded2, "nodes expanded")

    if expanded2 < expanded1:
        print("\nManhattan Distance expands fewer nodes.")
        print("It is a more informed admissible heuristic.")

    print("\nSolution using Manhattan Distance:")
    print_solution(path2)
