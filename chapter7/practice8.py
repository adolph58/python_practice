sandwich_orders = ['tuna', 'beaf', 'eggs']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print("所有三明治已经做好：")
for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich")
