
# importing tkinter
from tkinter import *
# importing Youtube module
from pytube import Youtube

# initializing tkinter
root = Tk()

# setting the geometry of the GUI

root.geometry("400*350")

# setting the title of the GUI

root.title("Youtube video downloader application")

# defining download function

def download():
    # using try and except to excute program without errors

    try:
        myVar.set("Downloading....")
        root.update()
        YouTube(link.get()).stremas.first().download()
        link.set("Video download successfully")
    
    except Exception as e:
        myVar.set("Mistake")
        root.update()
        link.set("Enter correct link")


