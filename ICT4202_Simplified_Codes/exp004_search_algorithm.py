# # Experiment 4: BFS, DFS, Bidirectional and Greedy Best-First Search
# from collections import deque
# from heapq import heappush, heappop

# graph = {
#     "A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "F"],
#     "D": ["B", "G"], "E": ["B", "G"], "F": ["C", "G"],
#     "G": ["D", "E", "F"]
# }
# h = {"A": 6, "B": 4, "C": 4, "D": 2, "E": 2, "F": 1, "G": 0}


# def bfs(g, start, goal):
#     q, seen = deque([[start]]), {start}
#     while q:
#         path = q.popleft()
#         node = path[-1]
#         if node == goal:
#             return path
#         for nxt in g[node]:
#             if nxt not in seen:
#                 seen.add(nxt)
#                 q.append(path + [nxt])


# def dfs(g, start, goal):
#     stack, seen = [[start]], set()
#     while stack:
#         path = stack.pop()
#         node = path[-1]
#         if node == goal:
#             return path
#         if node not in seen:
#             seen.add(node)
#             for nxt in reversed(g[node]):
#                 if nxt not in seen:
#                     stack.append(path + [nxt])


# def bidirectional(g, start, goal):
#     q1, q2 = deque([start]), deque([goal])
#     p1, p2 = {start: None}, {goal: None}
#     while q1 and q2:
#         for q, parents, other in ((q1, p1, p2), (q2, p2, p1)):
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 for nxt in g[node]:
#                     if nxt not in parents:
#                         parents[nxt] = node
#                         q.append(nxt)
#                         if nxt in other:
#                             left, x = [], nxt
#                             while x is not None:
#                                 left.append(x)
#                                 x = p1[x]
#                             right, x = [], p2[nxt]
#                             while x is not None:
#                                 right.append(x)
#                                 x = p2[x]
#                             return left[::-1] + right
#     return None


# def greedy(g, start, goal, heuristic):
#     q, seen = [(heuristic[start], [start])], set()
#     while q:
#         _, path = heappop(q)
#         node = path[-1]
#         if node == goal:
#             return path
#         if node not in seen:
#             seen.add(node)
#             for nxt in g[node]:
#                 if nxt not in seen:
#                     heappush(q, (heuristic[nxt], path + [nxt]))


# print("BFS:", bfs(graph, "A", "G"))
# print("DFS:", dfs(graph, "A", "G"))
# print("Bidirectional:", bidirectional(graph, "A", "G"))
# print("Greedy:", greedy(graph, "A", "G", h))




from collections import deque

def bfs(graph, start_node):
    visited = set([start_node])
    queue = deque([start_node])
    
    while queue:
        # Remove the first node added to the queue (FIFO)
        node = queue.popleft()
        print(node, end=" ")  # Process the node (e.g., print it)
        
        # Check all unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example Usage:
# The graph is represented as an Adjacency List (dictionary mapping nodes to lists of neighbors)
example_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS Traversal starting from 'A':")
bfs(example_graph, 'A')








# The graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
        
    # 1. Mark the current node as visited
    visited.add(node)
    print(node, end=" ")
    
    # 2. Recursively visit all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Run DFS starting from node 'A'
print("DFS Traversal:")
dfs(graph, 'A')
