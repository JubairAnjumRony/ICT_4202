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
