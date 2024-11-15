# sneaky-snake-AI
### Snake Game with Pathfinding Algorithms

## Project Overview
This project is an interactive snake game that uses three AI pathfinding algorithms to guide the snake toward the fruit:
1. **A\* (A-Star)**
2. **BFS (Breadth-First Search)**
3. **DFS (Depth-First Search)**

The game is implemented using **Pygame** and includes graphical and statistical features to showcase the performance of each algorithm.

---

## Features
- **Graphical Environment:** A visually appealing game interface designed with Pygame.
- **Pathfinding Algorithms:** Implementation of A\*, BFS, and DFS algorithms with real-time path visualization.
- **Dynamic Gameplay:**
  - Color-changing snake and animated fruit.
  - Adjustable game speed for enhanced player control.
- **Performance Metrics:** 
  - Displays the number of nodes visited and the time taken by each algorithm.
  - Highlights differences in algorithm efficiency through gameplay.

---
# Pathfinding Algorithms

## 1. A\* Algorithm
- **Description:**  
  A heuristic-based algorithm combining actual cost (g) and estimated cost to the goal (h) to efficiently find the shortest path.
- **Advantages:**  
  Guarantees the shortest path and performs efficiently with large grids and obstacles.
- **Use Case:**  
  Suitable for complex grid layouts where optimal solutions are required.

---

## 2. BFS Algorithm
- **Description:**  
  Explores paths level by level to find the shortest route.
- **Advantages:**  
  Guarantees the shortest path.
- **Disadvantages:**  
  Higher memory usage compared to A\*.
- **Use Case:**  
  Works well in simpler grids without complex obstacles.

---

## 3. DFS Algorithm
- **Description:**  
  Explores paths deeply before backtracking, often resulting in suboptimal solutions.
- **Advantages:**  
  Low memory usage.
- **Disadvantages:**  
  Does not guarantee the shortest path.
- **Use Case:**  
  Best suited for small grids or cases where path optimality is not critical.

