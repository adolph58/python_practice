from die import Die

print("6 面骰子结果：")
die_6 = Die()
for i in range(1, 11):
    die_6.roll_die()

print("10 面骰子结果：")
die_10 = Die(10)
for i in range(1, 11):
    die_10.roll_die()

print("20 面骰子结果：")
die_20 = Die(20)
for i in range(1, 11):
    die_20.roll_die()
