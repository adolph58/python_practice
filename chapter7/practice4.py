prompt = "Please input a pizza toppings: "

while True:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print(f"\nWe will add {toppings} to your pizza!")
