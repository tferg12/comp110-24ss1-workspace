"""One Shot Battleship."""

__author__ = "730460559"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

guess_row: int = int(input("Guess a row: "))

while guess_row > grid_size or guess_row < 1:
    guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

guess_column: int = int(input("Guess a column: "))

while guess_column > grid_size or guess_column < 1:
    guess_column = int(
        input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    )

blue_box: str = "\U0001F7E6"
red_box: str = "\U0001F7E5"
white_box: str = "\U00002B1C"
result: str = ""
row_counter: int = 1

while row_counter <= grid_size:
    emoji_str: str = ""
    column_counter: int = 1
    while column_counter <= grid_size:
        if guess_row == row_counter and guess_column == column_counter:
            if guess_row == secret_row and guess_column == secret_column:
                emoji_str += red_box
            else:
                emoji_str += white_box
        else:
            emoji_str += blue_box
        column_counter += 1
    print(emoji_str)
    row_counter += 1

if guess_row == secret_row and guess_column != secret_column:
    print("Close! Correct row, wrong column.")
elif guess_column == secret_column and guess_row != secret_row:
    print("Close! Correct column, wrong row.")

if guess_column == secret_column and guess_row == secret_row:
    print("Hit!")
else:
    print("Miss!")
