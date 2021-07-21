favorite_places = {
    'Jack': ['Shanghai', 'Beijing'],
    'Mary': ['New York', 'Paris'],
    'Lisi': ['Kaifeng', 'Xinyang'],
    }

for user, fp in favorite_places.items():
    print(f"Username: {user.title()}")
    for place in fp:
        print(f"\t{place}")
