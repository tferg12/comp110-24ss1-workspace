"""Practice with expressions and variables"""

print("comp110".isalpha())

print("110".isdigit())

print("comp110"[0].isalpha())

# print("adding incompatible types:")
# "Hello" + 1

# Example of declaring a variable
name: str = "Taylor"

# Accessing and printing a variable
print(name)

# Update Variable
name = "Ferguson"
print(name * 2)

# Numerical Variables
trail_a: int = 1
trail_b: int = 3
print(trail_a + trail_b)
total_miles: int = trail_a + trail_b
print(total_miles)

# Input

fav_color: str = input("What's your favorite color?")
print(fav_color + " is a cool color!")

lucky_number: int = int(input("What's your lucky number?"))
my_number: int = (lucky_number) + 1
print("My lucky number is " + str(my_number))
