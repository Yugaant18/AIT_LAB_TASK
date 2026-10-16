
# Task 7: Monkey Banana Problem using Goal Stack Planning

def move(subject, x1, x2):
    return f"Move {subject} from {x1} to {x2}"

def push_box(x1, x2):
    return f"Push box from {x1} to {x2}"

def climb_box(x, direction):
    return f"Climb box at {x} {direction}"

def have_banana(x):
    return f"Have banana at {x}"

# Initial state
initial_state = {
    "monkey_at": "A",
    "monkey_level": "down",
    "banana_at": "B",
    "box_at": "A",
    "has_banana": False
}

# Goal state
goal_state = {
    "has_banana": True
}

def plan_actions(initial_state, goal_state):
    actions = []

    if (initial_state["monkey_at"] == initial_state["box_at"]
            and initial_state["banana_at"] == "B"):

        actions.append(move("Monkey", "A", "B"))
        actions.append(push_box("A", "B"))
        actions.append(climb_box("B", "up"))
        actions.append(have_banana("B"))

    return actions

actions = plan_actions(initial_state, goal_state)

print("Plan:")
for action in actions:
    print(action)
