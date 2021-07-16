s1 = 'river'
s2 = 'sea'
if s1 == s2:
    print("两个字符串相等")
else:
    print("两个字符串不相等")

user = 'Join'
if user.lower() == 'join':
    print("用户已经存在，请重新选择一个用户名")

num1 = 12
num2 = 13
if num1 == num2:
    print("两个数字相等")
if num1 != num2:
    print("num1 不等于 num2")
if num1 > num2:
    print("num1 大于 num2")
if num1 < num2:
    print("num1 小于 num2")

if num1 > 10 and num2 > 10:
    print("num1 和 num2 都大于 10")
if num2 > 12 or num2 > 12:
    print("num1 和 num2 中有一个大于 12")

cars = ['audi', 'bmw', 'toyota', 'subaru']
if 'audi' in cars:
    print("Audi is in list!")

if 'honda' not in cars:
    print("Honda is not in list!")
