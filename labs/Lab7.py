from tinytag import TinyTag

print('please input a song file location')

location = input()

tag = TinyTag.get("C:/Users/airle/Music/American Idiot/Green Day - American Idiot.flac")
print('This track is by %s' % tag.artist)
print('The track is in the album %s' % tag.album)
print('The track is number %s' % tag.track )
print('The track is a %s Song' % tag.genre)