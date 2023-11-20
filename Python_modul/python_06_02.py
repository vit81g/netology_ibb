class Track:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    
    def show(self):
        print(f"<{self.title}-{self.duration}>")

class Album:
    def __init__(self, album_name, group):
        self.album_name = album_name
        self.group = group
        self.tracks = []
    
    def get_tracks(self):
        for track in self.tracks:
            track.show()
    
    def add_track(self, track):
        self.tracks.append(track)
    
    def get_duration(self):
        total_duration = 0
        for track in self.tracks:
            total_duration += track.duration
        return total_duration
        
    def print_tracks(self):
    	pass
    	
    	


# Создание треков
track1 = Track("Track 1", 4)
track2 = Track("Track 2", 3)
track3 = Track("Track 3", 5)

# Создание альбомов и добавление треков
album1 = Album("Album 1", "Group 1")
album1.add_track(track1)
album1.add_track(track2)
album1.add_track(track3)

track4 = Track("Track 4", 2)
track5 = Track("Track 5", 3)
track6 = Track("Track 6", 4)

album2 = Album("Album 2", "Group 2")
album2.add_track(track4)
album2.add_track(track5)
album2.add_track(track6)

# Вывод длительности альбомов
print(f"Длительность {album1.album_name}: {album1.get_duration()} минут")
print(f"Длительность {album2.album_name}: {album2.get_duration()} минут")
print(f"album2.print_tracks")
