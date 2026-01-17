# class definition
class Song:
   def __init__(self,performer,title,album,cover):
      self.performer = performer
      self.title = title
      self.album = album
      self.cover = cover
   def __str__(self):
      return f'Perfomer:\t{self.performer}\nTitle:\t\t{self.title}\nAlbum:\t\t{self.album}\nYear:\t\t{self.cover}'

# object creation
song1 = Song("Adele","Skyfall","Nwm","0000")
song2 = Song("Paktofonika","C.D Kinematografii","Archiwum Kinematografii","2010")

## object usage
print(song1)
print()
print(song2)