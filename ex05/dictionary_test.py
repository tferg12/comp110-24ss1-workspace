"""Dictionary Unit Tests."""

__author__ = "730460559"

from ex05.dictionary import (
    count,
    alphabetizer,
    invert,
    favorite_color,
    update_attendance,
)

import pytest


def test_count_edge_case() -> None:
    """Testing empty list in count function."""
    assert count([]) == {}


def test_count_use_case() -> None:
    """Testing count function with repeated letters."""
    a: list[str] = ["a", "a", "b", "b", "c"]
    assert count(a) == {"a": 2, "b": 2, "c": 1}


def test_count() -> None:
    """Testing count function with repeated words."""
    a: list[str] = ["yes", "no", "yes"]
    assert count(a) == {"yes": 2, "no": 1}


def test_alphbetizer_edge_case() -> None:
    """Testing empty list in alphabetizer."""
    assert alphabetizer([]) == {}


def test_alphabetizer_use_case() -> None:
    """Testing alphabetizer with keys not in alphabetical order."""
    a: list[str] = ["zebra", "ant", "yellow", "hat"]
    assert alphabetizer(a) == {"a": "ant", "h": "hat", "y": "yellow", "z": "zebra"}


def test_alphabetizer3() -> None:
    """Testing alphabetizer with keys in alphabetical order."""
    a: list[str] = ["ant", "hat", "see"]
    assert alphabetizer(a) == {"a": "ant", "h": "hat", "s": "see"}


def test_invert() -> None:
    """Testing invert with an empty list."""
    assert invert({}) == {}


def test_invert2() -> None:
    """Testing invert with two values the same."""
    with pytest.raises(KeyError):
        x = {"Taylor": "Ferguson", "Bristol": "Ferguson"}
        invert(x)


def test_invert3() -> None:
    """Testing invert function swaps keys and values."""
    a: dict[str, str] = {"cow": "moo", "pig": "oink"}
    assert invert(a) == {"moo": "cow", "oink": "pig"}


def test_favorite_color() -> None:
    """Testing favortie color with different colors."""
    a: dict[str, str] = {"Sal": "blue", "Ron": "red", "Roy": "white"}
    assert favorite_color(a) == "blue"


def test_favorite_color2() -> None:
    """Testing favorite color with a majority of one color."""
    a: dict[str, str] = {"Sal": "blue", "Ron": "red", "Roy": "red"}
    assert favorite_color(a) == "red"


def test_favorite_color3() -> None:
    """Testing favorite color with a tie."""
    a: dict[str, str] = {"Sal": "blue", "Bill": "blue", "Ron": "red", "Roy": "white"}
    assert favorite_color(a) == "blue"


def test_update_attendance() -> None:
    """Testing with same student names."""
    a: dict[str, list[str]] = {"Monday": ["Bill", "Ron"], "Tuesday": ["Sam"]}
    update_attendance(a, "Tuesday", "Sam")
    assert a == {"Monday": ["Bill", "Ron"], "Tuesday": ["Sam"]}


def test_update_attendance2() -> None:
    """Testing it adds students name to day."""
    a: dict[str, list[str]] = {"Monday": ["Bill", "Ron"], "Tuesday": ["Sam"]}
    update_attendance(a, "Tuesday", "Roy")
    assert a == {"Monday": ["Bill", "Ron"], "Tuesday": ["Sam", "Roy"]}


def test_update_attendance3() -> None:
    """Testing with empty dict."""
    a: dict[str, list[str]] = {}
    update_attendance(a, "Friday", "Dave")
    assert a == {"Friday": ["Dave"]}
