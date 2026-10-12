# Experiment 1: Intelligent Agents and Simple Reflex Agent

def agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"

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
