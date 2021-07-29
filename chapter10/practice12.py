import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    favorite_number = input("Input your favorite number: ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
        print(f"I'll remember your favorite number.")
else:
    print(f"I konw your favorite number! It's {favorite_number}")
