import re
import sys
from pytube import Playlist, YouTube, Search


def download():
    while True:
        print("\nWelcome to the ultimate youtube search and downloader \n")

        info = input(
            "Do you have a link already that you want to download? (y or n) \n"
        )

        inf = info.lower()

        yt = None  # Initialize yt variable outside the if-else block

        if re.search(r"y", inf):
            link = input("What's the YouTube link you want to download? \n")
            link_type = input("What type of link is it, playlist or video? \n")
            download_type = input("Download the video or just the audio? \n")

            dl = download_type.lower()
            typee = link_type.lower()

            if link != "":
                yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)

                if re.search(r"v", dl):
                    if re.search(r"list", typee):
                        playlist = Playlist(link)
                        for video in playlist.videos:
                            stream = video.streams.get_highest_resolution()
                            stream.download()
                            print(f"Downloading {video} ..... please wait\n")
                    elif re.search(r"vid", typee):
                        stream = yt.streams.get_highest_resolution()
                        stream.download()
                        print(f"Downloading {yt.title}.... please wait\n")
                    else:
                        decide = input(
                            "I didn't understand your response. Retry or quit? \n"
                        )
                        if re.search(r"q", decide.lower()):
                            sys.exit("\nHave a great day\n")
                        else:
                            continue
                elif re.search(r"a|m", dl):
                    if re.search(r"list", typee):
                        playlist = Playlist(link)
                        for video in playlist.videos:
                            stream = video.streams.get_audio_only()
                            stream.download()
                            print(f"Downloading audio from {video.title}")
                    elif re.search(r"vid", typee):
                        stream = yt.streams.get_audio_only()
                        stream.download()
                        print(f"Downloading audio from {yt.title}")
                    else:
                        decide = input(
                            "I didn't understand your response. Retry or quit? \n"
                        )
                        if re.search(r"q", decide.lower()):
                            sys.exit("\nHave a great day\n")
                        else:
                            continue
                else:
                    decide = input(
                        "I didn't understand your response. Retry or quit? \n"
                    )
                    if re.search(r"q", decide.lower()):
                        sys.exit("\nHave a great day\n")
                    else:
                        continue
            else:
                decide = input("I didn't understand your response. Retry or quit? \n")
                if re.search(r"q", decide.lower()):
                    sys.exit("\nHave a great day\n")
                else:
                    continue
        elif re.search(r"n", inf):
            msg = input("What do you want to search on YouTube? \n")
            decision = input("Download the video or just the audio? \n")

            s = Search(msg)

            if msg != "":
                url = s.results[0]
                idd = url.video_id
                link = "https://youtube.com/watch?v=" + idd

                yt = YouTube(link)

                if re.search(r"v", decision.lower()):
                    stream = yt.streams.get_highest_resolution()
                    stream.download()
                    print(f"Downloading {yt.title}.... please wait\n")

                elif re.search(r"a", decision.lower()):
                    stream = yt.streams.get_audio_only()
                    stream.download()
                    print(f"Downloading audio from {yt.title}\n")

                else:
                    teller = input("I don't understand.. do you wish to continue? \n")
                    if re.search(r"y", teller):
                        continue
                    sys.exit("Have a great day!!")
            else:
                teller = input("I don't understand.. do you wish to continue? \n")
                if re.search(r"y", teller):
                    continue
                sys.exit("Have a great day!!\n")

        else:
            tell = input("I don't understand.. do you wish to continue? \n")
            if re.search(r"y", tell):
                continue
            sys.exit("Have a great day!! \n")
