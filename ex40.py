class Song(object):

    def __init__(self, lyrics):
        self.lines = lyrics
    # the variable is initialized (set value to) lyrics which is the list below

    def sing_me_a_song(self):
        for line in self.lines: #already a list
            print(line)

happy_baby = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "with pockets full of shells"])

happy_baby.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
