#!/usr/bin/python3

def canUnlockAll(boxes):
    """keep track of visited boxes"""
    visited = set()

    """To perform first index search"""
    queue = [0]

    """update visited"""
    visited.add(0)

    """A loop to perform the search"""
    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key < len(boxes) and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == len(boxes)