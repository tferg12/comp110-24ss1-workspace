"""Exercise 4: List Utility Functions."""

__author__ = "730460559"


def all(x: list[int], y: int) -> bool:
    """Determines if all the ints are the same in both lists."""
    if len(x) == 0:
        return False
    idx = 0
    while idx < len(x):
        if x[idx] == y:
            idx += 1
        else:
            return False
    return True


def max(x: list[int]) -> int:
    """Returns the largest in list."""
    if len(x) == 0:
        raise ValueError("max() arg is an empty list")
    idx = 0
    z: int = x[0]
    while idx < len(x):
        if x[idx] > z:
            z = x[idx]
        idx += 1
        y: int = z
    return y


def is_equal(x: list[int], y: list[int]) -> bool:
    """Evaluates if every element at every index is equal."""
    if len(x) != len(y):
        return False
    idx = 0
    while idx < len(x):
        if x[idx] == y[idx]:
            idx += 1
        else:
            return False
    return True


def extend(x: list[int], y: list[int]) -> None:
    """Adds elements from y to x."""
    idx: int = 0
    while idx < len(y):
        x.append(y[idx])
        idx += 1
    return
