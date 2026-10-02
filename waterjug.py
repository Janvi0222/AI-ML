##waterjug

from collections import deque

jug1_capacity = 4
jug2_capacity = 3

initial_state = (0, 0)
visited = set()
queue = deque([initial_state])

print("State Space:")

while queue:
    state = queue.popleft()

    if state in visited:
        continue

    visited.add(state)

    x, y = state
    print(state)

    next_states = [
        (jug1_capacity, y),
        (x, jug2_capacity),
        (0, y),
        (x, 0)
    ]

    # Pour Jug 1 -> Jug 2
    transfer = min(x, jug2_capacity - y)
    next_states.append((x - transfer, y + transfer))

    # Pour Jug 2 -> Jug 1
    transfer = min(jug1_capacity - x, y)
    next_states.append((x + transfer, y - transfer))

    for next_state in next_states:
        if next_state not in visited:
            queue.append(next_state)

print("\nTotal Reachable States =", len(visited))
