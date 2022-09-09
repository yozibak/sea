from typing import List


def prompt(
    commands: List[str]
) -> int:
    for n, cmd in enumerate(commands):
        print(f"[{n}]: {cmd}")
    action = int(input()) or 0
    return action
