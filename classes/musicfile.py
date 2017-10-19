class Artist:
    def __init__(self, artist_name):
        self.songs = []
        self.name = artist_name

    def __str__(self):
        return self.name

    def add_songs(self, *args):
        self.songs.extend(args)


class MusicFile:
    def __init__(self, filename):
        self.filename = filename

    def artist(self, artist_name):
        art = Artist(artist_name)
        with open(self.filename, 'r') as music:
            for line in music.readlines():
                curr_name, title = line.split('-')
                print(curr_name, title)
                if curr_name.strip() == artist_name:
                    art.add_songs(title.strip())
        return art
