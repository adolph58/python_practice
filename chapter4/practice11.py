my_pizzas = ['pepperoni', 'beef', 'bacon', 'durian']
friend_pizzas = my_pizzas[:]
my_pizzas.append('fruit')
friend_pizzas.append('vegetables')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
