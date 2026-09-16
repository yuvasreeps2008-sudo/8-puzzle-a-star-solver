8-Puzzle Solver - Test Cases

This file contains test cases to verify the correctness of the 8-Puzzle A* Solver.

1. Test Heuristic Functions

Test 1: Goal State

Input:

1 2 3
4 5 6
7 8 0

Expected:

- Misplaced Tiles = 0
- Manhattan Distance = 0

Test 2: One Tile Out of Position

Input:

1 2 3
4 5 6
7 0 8

Expected:

- Misplaced Tiles = 1
- Manhattan Distance = 1

2. Test Neighbor Generation

Input:

1 2 3
4 0 5
6 7 8

Expected:

- The blank tile can move Up, Down, Left, and Right.
- Total valid neighboring states = 4.

3. Test A* Solver

Input:

1 2 3
4 5 6
0 7 8

Expected:

- A solution should be found.
- Solution cost = 2 moves.
- Both heuristics should produce an optimal solution.

4. Test Heuristic Comparison

Run the same puzzle using:

1. Misplaced Tiles
2. Manhattan Distance

Record:

- Solution cost
- Nodes expanded

Expected:

- Both should find an optimal solution.
- Manhattan Distance should provide a more informed estimate and may expand fewer nodes.

5. Test Goal State

Input:

1 2 3
4 5 6
7 8 0

Expected:

- Solution cost = 0
- Nodes expanded should be minimal.
- Both heuristics should return the goal immediately.

Conclusion

These test cases verify the heuristic calculations, neighbor generation, optimal solution, and comparison of the two A* heuristics.
