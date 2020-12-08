class Track:
    def __init__(self, name, duration=0):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'{self.name}-{self.duration}min'

    def __lt__(self, other):
        if not isinstance(other, Track):
            print('Not a Track')
        return self.duration < other.duration


class Album:
    def __init__(self, name, group, list_track):
        self.name = name
        self.group = group
        self.list_track = []

    def __str__(self):
        return f' Name group: {self.group}\n' \
               f' Name album: {self.name}\n' \
               f' Tracks: \n         {sound1}\n         {sound2}'


sound1 = Track('Твоя песня', 3.6)
sound2 = Track('Вторая песня', 3.3)
sound3 = Track('Третья песня', 3.7)
sound4 = Track('Твоя песня', 3.0)
sound5 = Track('Вторая песня', 3.1)
sound6 = Track('Третья песня', 3.9)

album1 = Album('Первый альбом', 'First group', [])
album2 = Album('Второй альбом', 'Second group', [])

print(album1)

print(sound2 < sound4)

