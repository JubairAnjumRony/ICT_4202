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
