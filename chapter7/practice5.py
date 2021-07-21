prompt = "Please tell me your age, I'll tell you your fare: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Your fare is free")
        elif age <= 12:
            print("Your fare is $10")
        else:
            print("Your fare is $15")
