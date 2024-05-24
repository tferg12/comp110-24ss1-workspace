"""While Counter Coding Challenge"""

message: str = "Banana"
idx: int = 0
amount_of_a: int = 0

while idx < len(message):
    print(message[idx])
    if message[idx] == "a":
        amount_of_a += 1
    idx += 1
print(f"The letter a shows up {amount_of_a} times")
