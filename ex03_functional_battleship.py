"""Functional Battleship."""

__author__ = "730460559"

from random import randint


def input_guess(grid_size: int, row_or_column: str) -> int:
    """Guess a row or column."""
    assert row_or_column == "row" or row_or_column == "column"
    guess: int = int(input(f"Guess a {row_or_column}: "))

    while guess > grid_size or guess < 1:
        guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return guess


def print_grid(
    grid_size: int, row_guess: int, column_guess: int, correct: bool
) -> None:
    """Print emoji grid."""
    blue_box: str = "\U0001F7E6"
    red_box: str = "\U0001F7E5"
    white_box: str = "\U00002B1C"
    row_counter: int = 1

    while row_counter <= grid_size:
        row_result: str = ""
        column_counter: int = 1
        while column_counter <= grid_size:
            if row_counter == row_guess and column_guess == column_counter:
                if correct:
                    row_result += red_box
                else:
                    row_result += white_box
            else:
                row_result += blue_box
            column_counter += 1
        print(row_result)
        row_counter += 1


def correct_guess(
    secret_row: int, secret_column: int, row_guess: int, column_guess: int
) -> bool:
    """Correct guess function."""
    if row_guess == secret_row and column_guess == secret_column:
        return True
    else:
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Main function."""
    turn_counter: int = 1
    while turn_counter <= 5:
        player_row: int = input_guess(grid_size, "row")
        player_column: int = input_guess(grid_size, "column")
        if correct_guess(secret_row, secret_column, player_row, player_column) is True:
            print(f"=== Turn {turn_counter}/5 ===")
            print_grid(grid_size, player_row, player_column, True)
            print(f"Hit! You won in {turn_counter}/5 turns!")
            turn_counter = 6
        if correct_guess(secret_row, secret_column, player_row, player_column) is False:
            print(f"=== Turn {turn_counter}/5 ===")
            print_grid(grid_size, player_row, player_column, False)
            print("Miss!")
            if turn_counter == 5:
                print("X/5 - Better luck next time!")
            else:
                print(f"{turn_counter}/5 - Better luck next time!")
        turn_counter += 1


if __name__ == "__main__":
    grid_size: int = randint(3, 5)
    main(grid_size, randint(1, grid_size), randint(1, grid_size))
