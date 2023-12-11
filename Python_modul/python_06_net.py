class Track:

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'{self.name}-{self.duration}min'

    def __eq__(self, other):
        return self.duration == other.duration

    def __gt__(self, other):
        return self.duration > other.duration

    def __lt__(self, other):
        return self.duration < other.duration

    def __ge__(self, other):
        return self.duration >= other.duration

    def __le__(self, other):
        return self.duration <= other.duration


class Album:

    def __init__(self, name, group, tracks):
        self.name = name
        self.group = group
        self.tracks = tracks

    def get_tracks(self):
        for track in self.tracks:
            track.show()

    def add_track(self, track):
        self.tracks.append(track)

    def get_duration(self):
        album_duration = 0
        for track in self.tracks:
            album_duration += track.duration
        print('Длительность альбома', album_duration)

    def __str__(self):
        s = f'Name group: {self.group}\n' \
            f'Name album: {self.name}\n' \
            f'Tracks:\n'
        for track in self.tracks:
            s += f'\t {track}\n'
        return s


violator_tracks = [Track('Personal Jesus', 5), Track('Enjoy the Silence', 4), Track('Clean', 3)]
violator = Album('Violator', 'Depeche Mode', violator_tracks)
violator.get_duration()
print(violator)

smiths_tracks = [Track('Reel Around the Fountain', 7), Track('Miserable Lie', 4), Track('Pretty Girls Make Graves', 3)]
smiths_album = Album('The Smiths', 'The Smiths', smiths_tracks)
smiths_album.get_duration()
print(smiths_album)

print(violator_tracks[0] > smiths_tracks[0])
print(violator_tracks[2] == smiths_tracks[2])
