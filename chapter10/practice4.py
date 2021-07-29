filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    while True:
        name = input("Enter your name: ")
        if name == 'exit':
            break
        else:
            file_object.write(name + '\n')
