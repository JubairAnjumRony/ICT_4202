from collections import deque      # FIFO queue: append on the right, popleft from the left
from heapq import heappush, heappop  # priority queue: always pops the smallest item

# Adjacency list: each node maps to the nodes it connects to
graph = {
    "A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "F"],
    "D": ["B", "G"], "E": ["B", "G"], "F": ["C", "G"],
    "G": ["D", "E", "F"]
}

# Estimated distance from each node to the goal G (used only by greedy)
heuristic = {"A": 6, "B": 4, "C": 4, "D": 2, "E": 2, "F": 1, "G": 0}


def bfs(graph, start, goal):
    queue = deque([[start]])        # queue of paths, starting with the path [start]
    visited = {start}               # nodes already queued, so we never queue them twice
    while queue:
        path = queue.popleft()      # take the oldest (shortest) path first
        node = path[-1]             # the last node on that path is where we are
        if node == goal:
            return path             # first time we reach the goal = shortest path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])   # extend the path by one step


def dfs(graph, start, goal):
    stack = [[start]]               # stack of paths, starting with [start]
    visited = set()
    while stack:
        path = stack.pop()          # take the newest path (last in, first out)
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            # reversed() pushes the last neighbor first, so the first neighbor
            # is popped first and the order matches the adjacency list
            for neighbor in reversed(graph[node]):
                stack.append(path + [neighbor])


def bidirectional(graph, start, goal):
    start_queue, goal_queue = deque([start]), deque([goal])
    start_parent, goal_parent = {start: None}, {goal: None}  # parent of each node on each side
    while start_queue and goal_queue:
        # Expand one full level from the start side, then one from the goal side
        for queue, parent, other_parent in (
            (start_queue, start_parent, goal_parent),
            (goal_queue, goal_parent, start_parent),
        ):
            for _ in range(len(queue)):          # process only the current level
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in parent:
                        parent[neighbor] = node  # remember how we got here
                        queue.append(neighbor)
                        if neighbor in other_parent:   # the two searches met
                            return build_bidirectional_path(
                                start_parent, goal_parent, neighbor
                            )
    return None                                   # no path exists


def build_bidirectional_path(start_parent, goal_parent, meet):
    # Walk from the meeting point back to start, then reverse the list
    left = []
    node = meet
    while node is not None:
        left.append(node)
        node = start_parent[node]
    # Walk from the meeting point forward to goal (skip the meeting node itself)
    right = []
    node = goal_parent[meet]
    while node is not None:
        right.append(node)
        node = goal_parent[node]
    return left[::-1] + right


def greedy(graph, start, goal, heuristic):
    heap = [(heuristic[start], [start])]   # (priority, path); lowest heuristic pops first
    visited = set()
    while heap:
        _, path = heappop(heap)            # pop the path whose last node looks closest to goal
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    heappush(heap, (heuristic[neighbor], path + [neighbor]))


print("BFS:", bfs(graph, "A", "G"))
print("DFS:", dfs(graph, "A", "G"))
print("Bidirectional:", bidirectional(graph, "A", "G"))
print("Greedy:", greedy(graph, "A", "G", heuristic))