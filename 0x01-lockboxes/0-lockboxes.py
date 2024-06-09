#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes. 
"""


def canUnlockAll(boxes):
    unlocked = set()
    unlocked.add(0)
    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                queue.append(key)
    return len(unlocked) == len(boxes)
