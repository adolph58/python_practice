while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        sum = int(first_number) + int(second_number)
        #first_number = int(first_number)
        #second_number = int(second_number)
    except ValueError:
        print("Please input a number")
    else:
        print(sum)
