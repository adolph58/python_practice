from random import randint,choice,sample

ticket_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']

def get_ticket():
    ticket = ''
    for i in range(1, 5):
        ticket += choice(ticket_list)
    return ticket
s = get_ticket()
print(f"本期彩票中奖号码是：{s}")

num = 0

while True:
    ticket = get_ticket()
    print(ticket)
    num += 1
    if ticket == s:
        print(f"你一共买了{num}张彩票")
        break
