
# Experiment 6: Heuristic Functions and A* Search

# Import functions for a priority queue.
# heappush() adds an item; heappop() removes the smallest item.
from heapq import heappush, heappop

# Define the graph.
# Each pair (neighbor, cost) represents an edge and its cost.
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("E", 1)],
    "D": [("G", 6)],
    "E": [("G", 3)],
    "G": []
}

# Heuristic values: estimated remaining cost from each node to G.
# The goal has heuristic value 0.
h = {
    "A": 7, "B": 6, "C": 3,
    "D": 6, "E": 2, "G": 0
}


# Define the A* search function.
def astar(graph, start, goal, h):

    # Priority queue entries contain:
    # (f-score, actual cost, current node, path)
    # f(n) = g(n) + h(n)
    # g(n) is the actual cost; h(n) is the estimated cost.
    q = [(h[start], 0, start, [start])]

    # Store the lowest known actual cost to reach each node.
    best = {start: 0}

    # Continue while the priority queue is not empty.
    while q:

        # Remove the entry with the smallest f-score.
        _, cost, node, path = heappop(q)

        # If the goal is reached, return its path and cost.
        if node == goal:
            return path, cost

        # Examine every neighbor of the current node.
        for nxt, step in graph[node]:

            # Calculate the actual cost of the new path.
            new_cost = cost + step

            # Continue only if this path is cheaper
            # than the previously recorded path to that neighbor.
            if new_cost < best.get(nxt, float("inf")):

                # Update the lowest known cost.
                best[nxt] = new_cost

                # Calculate f(n) = g(n) + h(n).
                # Add the new node and updated path to the queue.
                heappush(
                    q,
                    (new_cost + h[nxt],
                     new_cost,
                     nxt,
                     path + [nxt])
                )

    # If no path exists, return None and infinity.
    return None, float("inf")


# Run A* from node A to node G.
path, cost = astar(graph, "A", "G", h)

# Print the selected path and its total cost.
print("Path:", path)
print("Total cost:", cost)
