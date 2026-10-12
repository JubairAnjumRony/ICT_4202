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
