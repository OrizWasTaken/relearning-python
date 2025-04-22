def make_album(artist, album):
    """Build a dictionary containing information about an album."""
    return {'artist': artist.title(), 'album': album.title()}

while True:
    print("\nEnter 'q' at any time to stop.")

    title = input("What's an album you like? ")
    if title == 'q':
        break

    artist = input("Who's the artist? ")
    if artist == 'q':
        break
    
    album_info = make_album(artist, title)
    print(album_info)