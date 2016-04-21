class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

hb = ['Happy birthday to you', 'I don\'t want to get sued.']

bop =['They rally around the family.', 'With a pocket full of shells.']

happy_bday = Song(hb)

bulls_on_parade = Song(bop)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
