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
