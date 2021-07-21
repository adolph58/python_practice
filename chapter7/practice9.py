sandwich_orders = ['tuna', 'pastrami', 'pastrami', 'beaf', 'eggs', 'pastrami']
print("本店的五香烟熏牛肉卖完了")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print("所有三明治已经做好：")
for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich")

if 'pastrami' not in finished_sandwiches:
    print("完成列表中没有五香烟熏牛肉")
