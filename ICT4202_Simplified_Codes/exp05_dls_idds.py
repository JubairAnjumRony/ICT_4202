# Experiment 5: Depth-Limited Search and Iterative Deepening

tree = {                                  # Creates a search tree using a dictionary
    "S": ["A", "B"],                      # S has two children: A and B
    "A": ["C", "D"],                      # A has two children: C and D
    "B": ["E", "F"],                      # B has two children: E and F
    "C": [],                              # C has no children
    "D": ["G"],                            # D has one child: G, the goal
    "E": [],                              # E has no children
    "F": [],                              # F has no children
    "G": []                               # G has no children
}


def dls(graph, node, goal, limit, path=None):  # Defines Depth-Limited Search
    path = (path or []) + [node]            # Creates or updates the path by adding the current node

    if node == goal:                        # Checks whether the current node is the goal
        return path                         # Returns the path if the goal is found

    if limit == 0:                          # Checks whether the depth limit has been reached
        return None                         # Stops searching deeper if the goal was not found

    for nxt in graph[node]:                 # Loops through the children of the current node
        result = dls(                        # Calls DLS recursively for the next child
            graph,                          # Passes the same search tree
            nxt,                            # Makes the child the new current node
            goal,                           # Keeps the same goal node
            limit - 1,                      # Reduces the depth limit by one
            path                            # Passes the current path
        )

        if result:                          # Checks whether the recursive call found a path
            return result                   # Returns the successful path immediately

    return None                             # Returns None if no child leads to the goal


def iddfs(graph, start, goal, max_depth=10):  # Defines Iterative Deepening DFS
    for limit in range(max_depth + 1):       # Tries depth limits from 0 to max_depth
        result = dls(                        # Runs DLS with the current depth limit
            graph,                          # Passes the search tree
            start,                          # Starts searching from S
            goal,                           # Specifies the target node
            limit                           # Uses the current depth limit
        )

        if result:                          # Checks whether DLS found the goal
            return limit, result            # Returns the successful depth and path

    return None, None                       # Returns None values if the goal is not found


print("DLS limit 2:", dls(tree, "S", "G", 2))  # Searches for G with depth limit 2
print("DLS limit 3:", dls(tree, "S", "G", 3))  # Searches for G with depth limit 3
print("IDDFS:", iddfs(tree, "S", "G", 5))      # Runs IDDFS with maximum depth 5