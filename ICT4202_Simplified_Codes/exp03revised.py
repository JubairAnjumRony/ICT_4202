
# Experiment 3: First-Order Logic for Knowledge Representation

# Store parent-child relationships as pairs in a set.
# Example: ("Rahim", "Karim") means Rahim is Karim's parent.
parents = {
    ("Rahim", "Karim"),
    ("Karim", "Nadia"),
    ("Rahim", "Mina"),
    ("Mina", "Rafi")
}

# Find the children whose parent is Rahim.
# The condition checks whether parent == "Rahim".
# sorted() arranges the resulting names alphabetically.
children = sorted(
    child for parent, child in parents
    if parent == "Rahim"
)

# Find grandparent-grandchild relationships.
# p1 is a possible grandparent, c1 is their child.
# p2 is a possible parent, and c2 is their child.
# If c1 == p2, the two relationships form a chain:
# p1 -> c1 -> c2, so p1 is c2's grandparent.
grandparents = sorted(
    (p1, c2)
    for p1, c1 in parents
    for p2, c2 in parents
    if c1 == p2
)

# Display the children of Rahim.
print("Children of Rahim:", children)

# Display all grandparent-grandchild pairs.
print("Grandparent relations:", grandparents)
