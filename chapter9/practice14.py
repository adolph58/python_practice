from random import randint,choice

my_ticket = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']
print("本期彩票中奖号码是：")
s = ''
for i in range(1, 5):
    s += choice(my_ticket)
print(s)
