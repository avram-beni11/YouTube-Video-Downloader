from pytube import *
from pytube import YouTube

from tkinter import *
from tkinter import ttk

# link = YouTube("http://youtube.com/watch?v=2lAe1cqCOXo")

# # searchQuery = input("Enter Video: ")
# # search = Search(searchQuery)

# # len(search.results)
# # search.results

# print(link.title) #Prints video title
# print(link.thumbnail_url) #Prints thumbnail URL

# link.download()



root = Tk()
root.title("YouTube Video Downloader")
# def Download(link):
#     youtubeObject = YouTube(link)
#     youtubeObject = youtubeObject.streams.filter(progressive=True)
#     #youtubeTitle = youtubeObject.title
#     try:
#         #print("Downloading: ", youtubeTitle)
#         youtubeObject.download()
#     except:
#         print("An error has occurred")
#     print("Download is completed successfully")


# link = input("Enter the YouTube video URL: ")
# Download(link)

ttk.Frame(root, padding="3 3 12 12")
root.mainloop()