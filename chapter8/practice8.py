def make_album(musician_name, album_name, number=None):
    if number:
        album = {'musician': musician_name, 'album_name': album_name, 'number': number}
    else:
        album = {'musician': musician_name, 'album_name': album_name}
    return album

while True:
    print("\nPlease tell me a album:")
    print("(enter 'q' at any time to quit)")

    musician_name = input("Musician name: ")
    if musician_name == 'q':
        break
    album_name = input("Album name: ")
    if album_name == 'q':
        break

    number = input("Number: ")
    if number == 'q':
        break
    if number:
        number = int(number)
        album = make_album(musician_name, album_name, number)
    else:
        album = make_album(musician_name, album_name)
    print(album)
