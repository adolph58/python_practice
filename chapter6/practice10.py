favorite_numbers = {
    'Libai': [2, 4], 
    'Dufu': [4, 9], 
    'Hezhizhang': [9, 7], 
    'Wangwei': [6,8], 
    'Liqingzhao': [3, 6],
    }

for name, fn in favorite_numbers.items():
    print(f"Name: { name}")
    for number in fn:
        print(f"\t{number}")
