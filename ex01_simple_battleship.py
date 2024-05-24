"""EX01 - Simple Battleship"""

__author__ = 730460559

boat_location_str: str = input("Pick a secret boat location between 1 and 4:")
boat_location: int = int(boat_location_str)

if boat_location > 4:
    print("Error! " + boat_location_str + " too high!")
    exit()
if boat_location < 1:
    print("Error! " + boat_location_str + " too low!")
    exit()

guess_str: str = input("Guess a number between 1 and 4:")
guess: int = int(guess_str)

if guess > 4:
    print("Error! " + guess_str + " too high!")
    exit()
if guess < 1:
    print("Error! " + guess_str + " too low!")
    exit()

blue_box: str = "\U0001F7E6"
red_box: str = "\U0001F7E5"
white_box: str = "\U00002B1C"


if guess == boat_location:
    print("Correct! You hit the ship.")
    if guess == 1:
        print(red_box + blue_box + blue_box + blue_box)
    elif guess == 2:
        print(blue_box + red_box + blue_box + blue_box)
    elif guess == 3:
        print(blue_box + blue_box + red_box + blue_box)
    elif guess == 4:
        print(blue_box + blue_box + blue_box + red_box)
else:
    print("Incorrect! You missed the ship.")
    if guess == 1:
        print(white_box + blue_box + blue_box + blue_box)
    elif guess == 2:
        print(blue_box + white_box + blue_box + blue_box)
    elif guess == 3:
        print(blue_box + blue_box + white_box + blue_box)
    elif guess == 4:
        print(blue_box + blue_box + blue_box + white_box)
