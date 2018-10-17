def make_album(artist, album_name, tracks=''):
    """Creates a dictionary containing music album information"""
    album_name = {'artist name': artist, 'album name': album_name}
    if tracks:
        album_name['Number of tracks'] = tracks
    return album_name


while True:
    print('Hello! Lets build some albums!')
    print('enter q at any time to stop adding albums\n')

    album_add = input('What is the name of album you\'d like to add?')
    if album_add == 'q':
        break

    artist_add = input('And who is the artist?')
    if artist_add == 'q':
        break

    tracks_add = input("""How many tracks are there on this album? 
    If you don't know, just hit enter.""")
    if tracks_add == 'q':
        break

    print(make_album(artist=artist_add, album_name=album_add, tracks=tracks_add))
    exit = input('Would you like to make another?')
    if 'n' in exit:
        break


print(album_name)
