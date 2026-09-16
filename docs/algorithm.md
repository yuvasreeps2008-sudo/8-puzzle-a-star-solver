8-Puzzle Solver using A* Search

1. Overview

The 8-Puzzle is a sliding puzzle consisting of 8 numbered tiles and one blank space arranged in a 3×3 grid.

This project uses the A Search Algorithm* to find an optimal solution from an initial state to the goal state.

Two heuristics are implemented:

- Misplaced Tiles
- Manhattan Distance

2. A* Search

A* selects the next state using:

f(n) = g(n) + h(n)

Where:

- "g(n)" = cost from the initial state to the current state
- "h(n)" = estimated cost from the current state to the goal
- "f(n)" = total estimated cost

3. Misplaced Tiles Heuristic

This heuristic counts the number of tiles that are not in their correct positions.

h(n) = Number of misplaced tiles

The blank tile is not included in the calculation.

4. Manhattan Distance Heuristic

Manhattan Distance calculates the total number of horizontal and vertical moves required to place each tile in its correct position.

h(n) = Σ |current row - goal row| + |current column - goal column|

The blank tile is not included.

5. Comparison

Both heuristics are admissible, meaning they never overestimate the actual cost required to reach the goal.

Manhattan Distance provides more information about the distance of each tile from its goal position. Therefore, it generally guides A* more effectively and can expand fewer nodes than the Misplaced Tiles heuristic.

The program records the number of nodes expanded by each heuristic for comparison.

6. Expected Result

Heuristic| Solution| Nodes Expanded
Misplaced Tiles| Optimal| Recorded by program
Manhattan Distance| Optimal| Recorded by program

The exact number of expanded nodes depends on the input puzzle.

7. Conclusion

The project demonstrates how A* Search can solve the 8-Puzzle optimally using admissible heuristics. The comparison shows why a more informed heuristic such as Manhattan Distance can reduce unnecessary node expansions while still maintaining optimality.
