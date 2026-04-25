# 🎮 Tic Tac Toe AI (Minimax Algorithm)

A simple command-line Tic Tac Toe game in Python where you play against an **unbeatable AI** powered by the **Minimax algorithm**.

---

## 🚀 Features

* 🤖 AI opponent using Minimax (optimal moves)
* 🎯 Win / Loss / Draw detection
* 🖥️ Command-line interface
* ⚡ Lightweight and fast

---

## 🛠️ Tech Stack

* Python 3
* Standard Library (`math` module)

---

## 📂 Project Structure

```
TIC-TAC-TOE/
│── main.py      # Game logic
│── README.md    # Documentation
```

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```
git clone https://github.com/<your-username>/tic-tac-toe.git
cd tic-tac-toe
```

### 2️⃣ Run the game

```
python3 main.py
```

---

## 🎯 How to Play

* You are **X**
* AI is **O**
* Enter numbers from **1 to 9**:

```
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
```

* First player to align 3 marks wins 🏆

---

## 🧠 Algorithm

The AI uses the **Minimax algorithm**, which:

* Explores all possible moves
* Chooses the best outcome
* Makes the AI unbeatable

---

## 📸 Sample Gameplay

```
X | O | X
O | X |  
  |   | O
```

---

## ✨ Future Improvements

* 🎨 GUI version (Tkinter / Pygame)
* 🎚️ Difficulty levels
* 👥 Multiplayer mode

---

## 👩‍💻 Author

Gobikha Ramesh

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!








# 🚀 GPS-Based City Route Finder using A* Algorithm

### 📍 *(Artificial Intelligence Problem Solving Project)*

---

## 🎯 Objective

The objective of this project is to apply Artificial Intelligence problem-solving techniques to find the most optimal route between two locations in a city using search algorithms. The system simulates a GPS-based navigation system with intelligent pathfinding capabilities.

---

## 📖 Problem Description

This project focuses on designing a GPS-based navigation system that determines the most efficient route between two locations in a city. The city is modeled as a weighted graph or grid, where each node represents a location and each edge represents a path with an associated travel cost such as distance or time. Some paths may be blocked due to obstacles like traffic or construction.

The system allows users to interactively select a start location and a destination through a graphical interface. Using the **A*** (A-star) search algorithm, the system computes the optimal route by considering both the actual cost from the start node and a heuristic estimate of the remaining distance to the goal.

---

## 🗺️ Graph Representation

The city is represented as a 2D weighted grid:

* Each cell represents a node (location)
* Movement between cells represents edges (paths)
* Each edge has an associated cost

### Grid Values:

| Value | Meaning                     |
| ----- | --------------------------- |
| 0     | Normal road (cost = 1)      |
| -1    | Obstacle / Wall (blocked)   |
| 2-9   | Traffic zones (higher cost) |

### Movement:

* Up, Down, Left, Right

---

## ⚙️ Algorithms Used

### 🔹 A* Search Algorithm (Primary)

**Formula:**
f(n) = g(n) + h(n)

* g(n) → actual cost from start
* h(n) → heuristic estimate
* f(n) → total cost

---

### 🔹 Dijkstra’s Algorithm

* No heuristic
* Guarantees optimal path
* Slower than A*

---

### 🔹 Breadth-First Search (BFS)

* Uses queue
* Fast but ignores weights
* Not optimal for weighted graphs

---

## 📐 Heuristic Functions

### Manhattan Distance

|x1 - x2| + |y1 - y2|

### Euclidean Distance

√((x1 - x2)² + (y1 - y2)²)

---

## 📊 Algorithm Comparison

| Feature        | A*   | Dijkstra | BFS  |
| -------------- | ---- | -------- | ---- |
| Optimal Path   | Yes  | Yes      | No   |
| Uses Heuristic | Yes  | No       | No   |
| Speed          | Fast | Medium   | Fast |

---

## 🧩 Features

* Interactive grid UI
* Start (Green) & End (Red) nodes
* Obstacles and traffic weights
* A*, Dijkstra, BFS support
* Visualization & animation
* Displays path, cost, nodes explored

---

## ▶️ Execution Steps

```bash
git clone https://github.com/your-username/AI_ProblemSolving.git
cd AI_ProblemSolving
pip install -r requirements.txt
python app.py
```

Open browser:

```id="h8h3m2"
http://localhost:5000
```

---

## 📁 Project Structure

```bash
AI_ProblemSolving/
├── app.py
├── algorithms/
├── templates/
├── static/
├── images/
├── README.md
```

---

## 🌐 Live Demo

https://route-finder-bkpi.onrender.com

---

## 🖥 Screenshots

(Add your images here if needed)

---

## 👤 Author

Name: Gobikha
**Project:** AI Problem Solving

---

## 🏁 Conclusion

This project demonstrates how AI search algorithms can solve real-world navigation problems efficiently. The **A*** algorithm provides the best performance by combining actual cost and heuristic estimation.

---

