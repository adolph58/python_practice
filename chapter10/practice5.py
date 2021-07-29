filename = 'love_programming_book.txt'

with open(filename, 'w') as file_object:
    while True:
        reason = input("Enter why you love programming: ")
        if reason == 'exit':
            break
        else:
            file_object.write(reason + '\n')
