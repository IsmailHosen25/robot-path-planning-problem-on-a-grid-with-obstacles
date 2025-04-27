# Robot Path Planning problem on a grid with obstacles
## Problem Description
This is a robot path planning problem on a grid with obstacles (cells colored black).
The figure shows a 6×6 grid with obstacles at 6 cell locations. The robot can move up, down, left, or right in one move.
Each move has a cost of 1.

![Screenshot 2025-04-27 100209](https://github.com/user-attachments/assets/1adc936f-9e26-4503-aef7-eeb88ae051fe)

Suppose the robot wants to find the shortest cost path from start location S to the closest goal locations
marked by G using A* search algorithm. If there were a single goal an admissible heuristic would be the
Manhattan distance between the current location and the goal location (assuming there are no obstacles – this
ensures the Manhattan distance will be smaller than the actual cost making the heuristic admissible). However,
to solve the problem with more than one goal you need to have an admissible heuristic to the closest goal
location. But you do not know which goal location is the closest. (hint: you can find the Manhattan distance to
all the goal nodes and then construct a heuristic function from them)


Write a python program to find the shortest path to the closest goal location. Your code should work for any
grid of size smaller than 10 x 10.

## Heuristic
* For a single goal, an admissible heuristic is the Manhattan distance between the current location and the goal (ignoring obstacles).

* With multiple goals, the heuristic must remain admissible:
  * Find the Manhattan distance to all goal nodes.
  * Use the minimum Manhattan distance as the heuristic value.

## Task
Write a Python program that:

* Finds the shortest path to the closest goal location.

* Works for any grid smaller than 10×10.

## Sample Input
5 6          // Number of rows and columns

2 1          // Start (source) cell

3            // Number of goal locations

2 6          // Goal cell

4 3          // Goal cell

5 5          // Goal cell

6            // Number of blocked (obstacle) cells

2 2          // Blocked cell

4 2          // Blocked cell

2 3          // Blocked cell

3 3          // Blocked cell

3 5          // Blocked cell

4 5          // Blocked cell

## Sample Output
The output should be the sequence of moves:
L = Left, R = Right, U = Up, D = Down

Example:
D D D R R U
