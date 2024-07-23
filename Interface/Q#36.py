from abc import  ABC,abstractmethod
class Playable(ABC):
    @abstractmethod
    def play(self):
        pass
class Song(Playable):
    def __init__(self,name):
        self.name=name
    def play(self):
        print(f"Playing song {self.name}")
class Video(Playable):
    def __init__(self,name):
        self.name=name
    def play(self):
        print(f"Playing video {self.name}")

class Game(Playable):
    def __init__(self,name):
        self.name=name
    def play(self):
        print(f"Playing game {self.name}")
s = Song("Har dil ki awaz ")
s.play()

v = Video("The Great Khali")
v.play()

g = Game("PUBG")
g.play()

