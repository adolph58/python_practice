prompt = "If you could visit one place in the world, where would you go? "
while True:
    place = input(prompt)
    if place == 'quit':
        break
    else:
        print(f"You want to go {place}!")
