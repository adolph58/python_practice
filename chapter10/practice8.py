filenames = ['cats.txt', 'dogs.txt']

try:
    pets = []
    for filename in filenames:
        with open(filename) as f:
            names = f.readlines()
        for name in names:
            pets.append(name.strip())
except FileNotFoundError:
    print("File not found, please check filename")
else:
    print(pets)
