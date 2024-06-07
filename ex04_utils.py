"""Exercise 4: List Utility Functions"""

__author__ = "730460559"


def all(x: list[int], y: int) -> bool:
    for elem in x:
        if elem != y:
            return False
        else:
            return True


def max(x: list[int]) -> int:
    if len(x) == 0:
        raise ValueError("max() arg is an empty list")
    idx = 0
    z: int = x[0]
    while idx < len(x):
        if x[idx] >= z:
            z = x[idx]
        idx += 1
        y: int = z
    return y


def is_equal(x: list[int], y: list[int]) -> bool:
    for idx in range(0, len(x)):
        if x[idx] != y[idx]:
            return False
        else:
            return True


def extend(x: list[int], y: list[int]) -> None:
    for elem in y:
        x.append(elem)
