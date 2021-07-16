ordinals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for ordinal in ordinals:
    if ordinal == 1:
        print(f"{ordinal}st")
    elif ordinal == 2:
        print(f"{ordinal}nd")
    elif ordinal == 3:
        print(f"{ordinal}rd")
    else:
        print(f"{ordinal}th")
