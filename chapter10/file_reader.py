filename = 'pi_digits.txt'

with open(filename) as file_object:
    contents = file_object.read()
# rstrip() 方法删除字符串末尾的空白
print(contents.rstrip())

# 逐行读取
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
