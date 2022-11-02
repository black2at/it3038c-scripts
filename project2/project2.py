from tinytag import TinyTag
import csv
print('Please input a song file location')

location = input()

tag = TinyTag.get(location)

header = ['Song Name', 'Album Name', 'Artist', 'Track Number', 'Genre', 'bitrate', 'File Size'] 

rows = [[tag.title,tag.album,tag.artist,tag.track,tag.genre, '%s kBits/s' % tag.bitrate,'%s bytes' % tag.filesize]]

with open(tag.title, 'w') as f:

    write = csv.writer(f)

    write.writerow(header)
    write.writerows(rows)

