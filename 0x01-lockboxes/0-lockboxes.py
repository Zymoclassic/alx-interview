def canUnlockAll(boxes):
    visited = set()
    queue = [0]
    visited.add(0)

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key < len(boxes) and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == len(boxes)