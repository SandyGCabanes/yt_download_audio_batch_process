


import youtube_dl
import time

def download_audio(url, output_path):

    # Options for downloading audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path + '/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Audio download finished.  Check your destination folder.")


# Input list of http addresses as a list

print ("Reminder: create a txt file in C:/temp/audio")
time.sleep (10)
print ("Name it as 'list_of_addresses.txt'")
time.sleep (10)

# opening the file in read mode
my_file = open("C:/temp/audio/list_of_addresses.txt", "r")

# reading the file
data = my_file.read()

# replacing end splitting the text when newline (\n) is seen
# in location of addresses or LOFA
lofa = data.split("\n")
print(lofa)
my_file.close()

numitems = len(lofa)
print ("There are ", numitems, " files.")


i = 0
while i < len(lofa):

    url = lofa[i]

    output_path = "C:/temp/audio"

    download_audio(url, output_path)

    print (i+1, " of ", numitems)

    i = i+1

print ("End of process")


