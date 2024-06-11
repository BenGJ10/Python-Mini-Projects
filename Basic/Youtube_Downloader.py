# make sure the pytube version == 12.1.0
from pytube import YouTube

try:
    url = input("Enter a valid YouTube url: ")
    yt = YouTube(url)  # create an object for YouTube

    print(f"Video Title: {yt.title}")
    print(f"View count: {yt.views}") 

    yd = yt.streams.get_highest_resolution()  # get highest video resolution

    yd.download("/Users/bengj/Downloads/ YT Downloads")
    print("Download complete.")

except Exception as exep:
    print("An error occured:", str(exep)) # incase an error occurs during the download