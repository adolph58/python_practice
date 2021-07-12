names = ['Buffett', 'Zhenyu Luo', 'Jun Wu']
print(f"{names[0]}:\nI want to invite you to dinner!")
print(f"{names[1]}:\nI want to invite you to dinner!")
print(f"{names[2]}:\nI want to invite you to dinner!")

names.insert(0, "Bill")
names.insert(2, "Lei Zhang")
names.append("Bai Lee")

print(f"{names[0]}:\nI want to invite you to dinner!")
print(f"{names[1]}:\nI want to invite you to dinner!")
print(f"{names[2]}:\nI want to invite you to dinner!")
print(f"{names[3]}:\nI want to invite you to dinner!")
print(f"{names[4]}:\nI want to invite you to dinner!")
print(f"{names[5]}:\nI want to invite you to dinner!")

name = names.pop()
print(f"{name}:\nI'm so sorry,I can't invite you!")
name = names.pop()
print(f"{name}:\nI'm so sorry,I can't invite you!")
name = names.pop()
print(f"{name}:\nI'm so sorry,I can't invite you!")
name = names.pop()
print(f"{name}:\nI'm so sorry,I can't invite you!")

print(f"{names[0]}:\nYou are still in invite list.")
print(f"{names[1]}:\nYou are still in invite list.")

del names[0]
del names[0]

print(names)
