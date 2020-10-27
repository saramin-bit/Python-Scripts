try:
    from pytube import YouTube
    from pytube import Playlist
except ModuleNotFoundError:
    exit("Please Download pytube from Github\nCommand:\tpip install git+https://github.com/nficano/pytube.git")


def download_video(youtube_url):
    youtube = YouTube(url)
    print(f"\n\nTitle of the video : {youtube.title}")
    available_quality = youtube.streams
    print("\n\n****----Available Video/Audio Types----****")
    for index, item in enumerate(available_quality):
        print(f"{index}) {available_quality[index].mime_type} "
              f"{'Resolution: ' + available_quality[index].resolution if available_quality[index].resolution else ''} "
              f"{'bit rate: ' + available_quality[index].abr if available_quality[index].abr else ''}")

    user_request = int(input("\nSelect Preferred Video/Audio type by number: "))
    try:
        user_request = available_quality[user_request]
    except ValueError:
        print("Enter wrong value")
        return False
    print("file size {:.2f}Mb".format(user_request.filesize / (1024 * 1024)))
    confirm = input("Are you want to download? [y / Any]: ")
    if not confirm.lower() == "y":
        return False
    print("Downloading ...")
    user_request.download()
    print("Download Success")
    return True


def main(url):
    download = False
    try:
        download = download_video(url)
        # sleep(5)
    except KeyboardInterrupt:
        exit("Ending The Script")
    except Exception as e:
        print("Error: ", e)
    finally:
        return download


if __name__ == '__main__':
    url = input("Enter the Full Youtube Video/Playlist Url: ")
    if "playlist" in url:
        print("Requesting Meta Information ...")
        play_list = Playlist(url)
        if len(play_list) == 0:
            exit("Sorry Cannot Find Video. Try again..")
        print("Total Video(s) in the playlist: ", len(play_list))
        selection = int(input("1) Download All video at once?\n2) Select Resolution one by one\nSelection[1/2]: "))
        if selection == 1:
            res = input("Enter Preferred Video Resolution [eg: 720p, 480p, 360p, 240p, 144p] : ")
            play_list.download_all(resolution=res)
            print("Video Downloaded SuccessFully")
        else:
            success = 0
            for url in play_list:
                if main(url):
                    success += 1
                else:
                    print("Skipping ")
            print(f"Total Video Download: {success}/{len(play_list)}")
    else:
        print("Requesting Meta Information ...")
        if main(url):
            print("Video Downloaded SuccessFully")
