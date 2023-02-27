import re
import sys
from pytube import Playlist, YouTube, Search


def download():

    while True:

        print("\nWelcome to the ultimate youtube search and downloader \n")

        info = input(
            "Do you have a link already that you want to download? (y or n) \n")

        inf = info.lower()

        if re.search(r'y', inf):

            link = input("What's the youtube link you want to download? \n")
            link_type = input("What type of link is it, playlist or video? \n")
            download_type = input("Download the video or just the audio? \n")

            dl = download_type.lower()

            typee = link_type.lower()

            if re.search(r'v', dl) and link != "":
                playlist = Playlist(link)
                yt = YouTube(link)

                if re.search(r'list', typee):

                    # Iterate over the playlist video URLs and download each video at highest quality
                    for video in playlist.videos:
                        stream = video.streams.get_highest_resolution()
                        stream.download()
                        print(f"Download {video} ..... please wait\n")

                elif re.search(r'vid', typee):

                    stream = yt.streams.get_highest_resolution()
                    stream.download()
                    print(f"Downloading {yt.title}.... please wait\n")

                else:
                    decide = input(
                        "I didn't understand your response. Retry or quit? \n")

                    if re.search(r'q', decide.lower()):
                        sys.exit("\nHave a great day\n")
                    else:
                        continue

            elif re.search(r'a|m', dl) and link != "":

                if re.search(r'list', typee):

                    for video in playlist.videos:
                        stream = video.streams.get_audio_only()
                        stream.download()
                        print(f'Downloading audio from {yt.title}')

                elif re.search(r'vid', typee):
                    stream = yt.streams.get_audio_only()
                    stream.download()
                    print(f'Downloading audio from {yt.title}')

                else:
                    decide = input(
                        "I didn't understand your response. Retry or quit? \n")

                    if re.search(r'q', decide.lower()):
                        sys.exit("\nHave a great day\n")
                    else:
                        continue
            else:
                decide = input(
                    "I didn't understand your response. Retry or quit? \n")

                if re.search(r'q', decide.lower()):
                    sys.exit("\nHave a great day\n")
                else:
                    continue
        elif re.search(r'n', inf):
            msg = input('What do you want to search on youtube? \n')
            decision = input("Download the video or just the audio? \n")

            s = Search(msg)

            if msg != "":

                for url in s.results:
                    idd = url.video_id
                    link = 'https://youtube.com/watch?v=' + idd

                    yt = YouTube(link)

                    if re.search(r'v', decision.lower()):
                        stream = yt.streams.get_highest_resolution()
                        stream.download()
                        print(f"Downloading {yt.title}.... please wait\n")

                    elif re.search(r'a', decision.lower()):
                        stream = yt.streams.get_audio_only()
                        stream.download()
                        print(f'Downloading audio from {yt.title}\n')

                    else:
                        teller = input(
                            "I don't understand.. do you wish to continue? \n")

                        if re.search(r'y', teller):
                            continue
                        sys.exit("Have a great day!!")

            else:
                teller = input(
                    "I don't understand.. do you wish to continue? \n")

                if re.search(r'y', teller):
                    continue
                sys.exit("Have a great day!!\n")
        else:
            tell = input("I don't understand.. do you wish to continue? \n")

            if re.search(r'y', tell):
                continue
            sys.exit("Have a great day!! \n")
