"""Dictionary Exercise 5."""

__author__ = "730460559"


def count(x: list[str]) -> dict[str, int]:
    """Counts number of times value appears."""
    a: dict[str, int] = {}
    if len(x) == 0:
        return {}
    for elem in x:
        if elem in a:
            a[elem] += 1
        else:
            a[elem] = 1
    return a


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    """Creates dictionary of alphabet letter keys and values from list."""
    y: dict[str, list[str]] = {}
    if len(x) == 0:
        return {}
    for elem in x:
        z = elem[0].lower()
        if z in y:
            y[z].append(elem)
        else:
            y[z] = [elem]
    return y


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values."""
    y: dict[str, str] = {}
    for key in x:
        if x[key] in y:
            raise KeyError
        else:
            y[x[key]] = key
    return y


def favorite_color(x: dict[str, str]) -> str:
    """Returns color that appears the most."""
    color_count = 0
    fav_color: str = ""
    fav_colors: dict[str, int] = {}

    for key in x:
        if x[key] in fav_colors:
            fav_colors[x[key]] += 1
        else:
            fav_colors[x[key]] = 1

    for key in fav_colors:
        if fav_colors[key] > color_count:
            color_count = fav_colors[key]
            fav_color = key
    return fav_color


def update_attendance(x: dict[str, list[str]], day: str, student: str) -> None:
    """Attendance function."""
    if day in x:
        if student not in x[day]:
            x[day].append(student)
    else:
        x[day] = [student]
