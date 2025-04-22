def make_album(artist, album, num_songs=None):
    """Build a dictionary containing information about an album."""

    album_info =  {'artist': artist.title(), 'album': album.title()}
    if num_songs:
        album_info['number of songs'] = num_songs
    return album_info


album = make_album('kendrick', 'GNX')
album['album'] = album['album'].upper()
print(album)

album = make_album( 'drake', 'certified lover boy')
print(album)

album = make_album('gunna', 'one of won')
print(album)

album = make_album('arrdee', 'pier pressure', 14)
print(album)