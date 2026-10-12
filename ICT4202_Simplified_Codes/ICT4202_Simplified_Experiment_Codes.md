# ICT-4202 AI/ML Laboratory: Simplified Codes

The codes follow the experiment serial numbers in the supplied manual. Experiment 7 uses WEKA Explorer, not Python. See `exp07_weka_steps.txt`.

Install the required packages once: `python -m pip install numpy matplotlib scikit-learn`

## EXPERIMENT 1: Intelligent Agents and a Simple Reflex Agent

```python
# Experiment 1: Intelligent Agents and Simple Reflex Agent

def agent(location, status):
    if status == "Dirty":
        return "Suck"
    return "Right" if location == "A" else "Left"

rooms = {"A": "Dirty", "B": "Dirty"}
location = "A"

for step in range(6):
    status = rooms[location]
    action = agent(location, status)
    print(step + 1, location, status, "->", action)

    if action == "Suck":
        rooms[location] = "Clean"
    elif action == "Right":
        location = "B"
    else:
        location = "A"

print("Final environment:", rooms)
```

## EXPERIMENT 2: Knowledge-Based Agents and Propositional Logic

```python
# Experiment 2: Knowledge-Based Agents and Propositional Logic

facts = {"Rain"}
rules = [
    ({"Rain"}, "WetGround"),
    ({"WetGround"}, "Slippery"),
    ({"Slippery"}, "DriveSlowly")
]

while True:
    changed = False
    for conditions, result in rules:
        if conditions <= facts and result not in facts:
            facts.add(result)
            print(conditions, "=>", result)
            changed = True
    if not changed:
        break

print("Inferred knowledge:", sorted(facts))
```

## EXPERIMENT 3: First-Order Logic for Knowledge Representation

```python
# Experiment 3: First-Order Logic for Knowledge Representation

parents = {
    ("Rahim", "Karim"), ("Karim", "Nadia"),
    ("Rahim", "Mina"), ("Mina", "Rafi")
}

children = sorted(child for parent, child in parents if parent == "Rahim")
grandparents = sorted((p1, c2) for p1, c1 in parents
                      for p2, c2 in parents if c1 == p2)

print("Children of Rahim:", children)
print("Grandparent relations:", grandparents)
```

## EXPERIMENT 4: BFS, DFS, Bidirectional and Greedy Best-First Search

```python
# Experiment 4: BFS, DFS, Bidirectional and Greedy Best-First Search
from collections import deque
from heapq import heappush, heappop

graph = {
    "A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "F"],
    "D": ["B", "G"], "E": ["B", "G"], "F": ["C", "G"],
    "G": ["D", "E", "F"]
}
h = {"A": 6, "B": 4, "C": 4, "D": 2, "E": 2, "F": 1, "G": 0}


def bfs(g, start, goal):
    q, seen = deque([[start]]), {start}
    while q:
        path = q.popleft()
        node = path[-1]
        if node == goal:
            return path
        for nxt in g[node]:
            if nxt not in seen:
                seen.add(nxt)
                q.append(path + [nxt])


def dfs(g, start, goal):
    stack, seen = [[start]], set()
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path
        if node not in seen:
            seen.add(node)
            for nxt in reversed(g[node]):
                if nxt not in seen:
                    stack.append(path + [nxt])


def bidirectional(g, start, goal):
    q1, q2 = deque([start]), deque([goal])
    p1, p2 = {start: None}, {goal: None}
    while q1 and q2:
        for q, parents, other in ((q1, p1, p2), (q2, p2, p1)):
            for _ in range(len(q)):
                node = q.popleft()
                for nxt in g[node]:
                    if nxt not in parents:
                        parents[nxt] = node
                        q.append(nxt)
                        if nxt in other:
                            left, x = [], nxt
                            while x is not None:
                                left.append(x)
                                x = p1[x]
                            right, x = [], p2[nxt]
                            while x is not None:
                                right.append(x)
                                x = p2[x]
                            return left[::-1] + right
    return None


def greedy(g, start, goal, heuristic):
    q, seen = [(heuristic[start], [start])], set()
    while q:
        _, path = heappop(q)
        node = path[-1]
        if node == goal:
            return path
        if node not in seen:
            seen.add(node)
            for nxt in g[node]:
                if nxt not in seen:
                    heappush(q, (heuristic[nxt], path + [nxt]))


print("BFS:", bfs(graph, "A", "G"))
print("DFS:", dfs(graph, "A", "G"))
print("Bidirectional:", bidirectional(graph, "A", "G"))
print("Greedy:", greedy(graph, "A", "G", h))
```

## EXPERIMENT 5: Depth-Limited Search and Iterative Deepening

```python
# Experiment 5: Depth-Limited Search and Iterative Deepening

tree = {
    "S": ["A", "B"], "A": ["C", "D"], "B": ["E", "F"],
    "C": [], "D": ["G"], "E": [], "F": [], "G": []
}


def dls(graph, node, goal, limit, path=None):
    path = (path or []) + [node]
    if node == goal:
        return path
    if limit == 0:
        return None
    for nxt in graph[node]:
        result = dls(graph, nxt, goal, limit - 1, path)
        if result:
            return result
    return None


def iddfs(graph, start, goal, max_depth=10):
    for limit in range(max_depth + 1):
        result = dls(graph, start, goal, limit)
        if result:
            return limit, result
    return None, None


print("DLS limit 2:", dls(tree, "S", "G", 2))
print("DLS limit 3:", dls(tree, "S", "G", 3))
print("IDDFS:", iddfs(tree, "S", "G", 5))
```

## EXPERIMENT 6: Heuristic Functions and A* Search

```python
# Experiment 6: Heuristic Functions and A* Search
from heapq import heappush, heappop

graph = {
    "A": [("B", 1), ("C", 4)], "B": [("D", 2), ("E", 5)],
    "C": [("E", 1)], "D": [("G", 6)], "E": [("G", 3)], "G": []
}
h = {"A": 7, "B": 6, "C": 3, "D": 6, "E": 2, "G": 0}


def astar(graph, start, goal, h):
    q, best = [(h[start], 0, start, [start])], {start: 0}
    while q:
        _, cost, node, path = heappop(q)
        if node == goal:
            return path, cost
        for nxt, step in graph[node]:
            new_cost = cost + step
            if new_cost < best.get(nxt, float("inf")):
                best[nxt] = new_cost
                heappush(q, (new_cost + h[nxt], new_cost, nxt, path + [nxt]))
    return None, float("inf")


path, cost = astar(graph, "A", "G", h)
print("Path:", path)
print("Total cost:", cost)
```

## EXPERIMENT 8: Supervised Learning, Linear Regression

```python
# Experiment 8: Supervised Learning - Linear Regression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([3, 5, 7, 9, 11, 13])

model = LinearRegression().fit(X, y)
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Prediction for 7 hours:", model.predict([[7]])[0])
print("R^2:", model.score(X, y))

plt.scatter(X[:, 0], y, label="Observed")
plt.plot(X[:, 0], model.predict(X), label="Fitted line")
plt.xlabel("Study hours")
plt.ylabel("Score")
plt.legend()
plt.show()
```

## EXPERIMENT 9: k-NN and Decision Tree Classification

```python
# Experiment 9: k-NN and Decision Tree Classification
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

models = [
    ("k-NN", KNeighborsClassifier(n_neighbors=5)),
    ("Decision Tree", DecisionTreeClassifier(max_depth=3, random_state=42))
]

for name, model in models:
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(name, "accuracy:", accuracy_score(y_test, pred))
    print(confusion_matrix(y_test, pred))
```

## EXPERIMENT 10: Unsupervised Learning, K-means Clustering

```python
# Experiment 10: Unsupervised Learning - K-means Clustering
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X = load_iris().data[:, :2]  # first two features
model = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = model.fit_predict(X)

print("Centers:\n", model.cluster_centers_)
print("Inertia:", model.inertia_)
print("Silhouette:", silhouette_score(X, labels))

plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1],
            marker="X", s=180, edgecolors="black")
plt.xlabel("Sepal length (cm)")
plt.ylabel("Sepal width (cm)")
plt.title("K-means clustering, k=3")
plt.show()
```

## EXPERIMENT 7: Introduction to WEKA for AI/ML Experiments

1. Open WEKA → Explorer → Preprocess → Open file.
2. Load the sample `iris.arff` dataset.
3. Confirm it has 150 instances and that the final attribute is the class.
4. Select Classify → Choose → trees → J48.
5. Choose 10-fold Cross-validation and click Start.
6. Record accuracy, correct/incorrect instances, Kappa, per-class statistics, and the confusion matrix.
7. Repeat with lazy → IBk, then compare results.
8. Save or copy the result buffer for the lab report.
