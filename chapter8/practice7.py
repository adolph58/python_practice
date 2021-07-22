def make_album(musician_name, album_name, number=None):
    if number:
        album = {'musician': musician_name, 'album_name': album_name, 'number': number}
    else:
        album = {'musician': musician_name, 'album_name': album_name}
    return album

print(make_album('Nirvana', 'Dive'))
print(make_album('Beatles', 'Yellow Submarine'))
print(make_album('Xuwei', 'guxiang', 8))
